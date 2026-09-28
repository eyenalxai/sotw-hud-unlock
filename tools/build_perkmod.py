#!/usr/bin/env python3
"""Build the SOTW HUD Unlock plugin (SOTW_HUDUnlock.esp).

The plugin is a light plugin (ESL). It has no scripts. It only overrides
four global variables (GLOB records):

  SkillsOfTheWild.esp : 0x000956 _WWW_PerkRank_SixthSense         = 1.0
  SkillsOfTheWild.esp : 0x000958 _WWW_PerkRank_SpatialAwareness   = 1.0
  ImmersiveHUD.esp    : 0x000EEE iHUD_DisableCompass              = 0.0
  ImmersiveHUD.esp    : 0x000FFF iHUD_DisableSneak                = 0.0

Usage:
    python build_perkmod.py [output_path]

The default output path is SOTW_HUDUnlock.esp in the repository root.
"""

import os
import struct
import sys

VERSION = "2.2.1"
AUTHOR = "eyenalxai"
SNAM = (
    "SOTW HUD Unlock %s. Shows the compass, the sneak meter and the crosshair "
    "for Skills of the Wild with ImmersiveHUD." % VERSION
)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(HERE), "SOTW_HUDUnlock.esp")

# Masters in load order. The patch is a master on purpose: this plugin
# must load after the patch that sets the two ImmersiveHUD locks.
MASTERS = [
    "Skyrim.esm",
    "SkillsOfTheWild.esp",
    "ImmersiveHUD.esp",
    "SOTW_ImmersiveHUD-SKSE_Patch.esp",
]

# (form id, editor id, FNAM type, value)
RECORDS = [
    (0x01000956, "_WWW_PerkRank_SixthSense", b"s", 1.0),
    (0x01000958, "_WWW_PerkRank_SpatialAwareness", b"s", 1.0),
    (0x02000EEE, "iHUD_DisableCompass", b"f", 0.0),
    (0x02000FFF, "iHUD_DisableSneak", b"f", 0.0),
]


def field(sig, data):
    return sig + struct.pack("<H", len(data)) + data


def zstr(s):
    return s.encode("cp1252") + b"\x00"


def glob(fid, edid, fnam, value):
    body = field(b"EDID", zstr(edid)) + field(b"FNAM", fnam) + field(b"FLTV", struct.pack("<f", value))
    hdr = (
        b"GLOB"
        + struct.pack("<I", len(body))
        + struct.pack("<I", 0)
        + struct.pack("<I", fid)
        + struct.pack("<I", 0)
        + struct.pack("<H", 43)
        + struct.pack("<H", 0)
    )
    return hdr + body


def build():
    records = b"".join(glob(*r) for r in RECORDS)
    grup = b"GRUP" + struct.pack("<I", 24 + len(records)) + b"GLOB" + struct.pack("<I", 0) + b"\x00" * 8

    hedr = struct.pack("<f", 1.71) + struct.pack("<I", len(RECORDS)) + struct.pack("<I", 0x800)
    payload = field(b"HEDR", hedr) + field(b"CNAM", zstr(AUTHOR)) + field(b"SNAM", zstr(SNAM))
    for m in MASTERS:
        payload += field(b"MAST", zstr(m)) + field(b"DATA", b"\x00" * 8)
    payload += field(b"INTV", struct.pack("<I", 1))

    tes4 = (
        b"TES4"
        + struct.pack("<I", len(payload))
        + struct.pack("<I", 0x200)  # 0x200 = light plugin (ESL)
        + b"\x00" * 4
        + b"\x00" * 4
        + struct.pack("<H", 44)
        + struct.pack("<H", 0)
        + payload
    )
    return tes4 + grup + records


def validate(path):
    """Read the plugin again and print its data. This finds structure errors."""
    d = open(path, "rb").read()
    size = struct.unpack_from("<I", d, 4)[0]
    flags = struct.unpack_from("<I", d, 8)[0]
    fv = struct.unpack_from("<H", d, 20)[0]
    q = 24
    masters = []
    while q < 24 + size:
        fs = d[q:q + 4]
        fl = struct.unpack_from("<H", d, q + 4)[0]
        fd = d[q + 6:q + 6 + fl]
        if fs == b"MAST":
            masters.append(fd.rstrip(b"\x00").decode("cp1252", "replace"))
        q += 6 + fl
    print("TES4 flags=0x%X formver=%d masters=%s" % (flags, fv, masters))
    pos = 24 + size
    while pos + 24 <= len(d):
        sig = d[pos:pos + 4]
        sz = struct.unpack_from("<I", d, pos + 4)[0]
        if sig == b"GRUP":
            print("GRUP label=%r size=%d" % (d[pos + 8:pos + 12], sz))
            pos += 24
            continue
        fid = struct.unpack_from("<I", d, pos + 12)[0]
        body = d[pos + 24:pos + 24 + sz]
        edid = fnam = fltv = None
        q = 0
        while q + 6 <= len(body):
            fs = body[q:q + 4]
            fl = struct.unpack_from("<H", body, q + 4)[0]
            fd = body[q + 6:q + 6 + fl]
            if fs == b"EDID":
                edid = fd.split(b"\x00")[0].decode("cp1252", "replace")
            if fs == b"FNAM":
                fnam = fd
            if fs == b"FLTV":
                fltv = struct.unpack("<f", fd)[0]
            q += 6 + fl
        mi = fid >> 24
        print("REC %s 0x%08X [%s:%06X] edid=%r FNAM=%r FLTV=%r" % (
            sig.decode("cp1252", "replace"), fid, masters[mi] if mi < len(masters) else "?",
            fid & 0xFFFFFF, edid, fnam, fltv))
        pos += 24 + sz


if __name__ == "__main__":
    data = build()
    out_dir = os.path.dirname(OUT)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUT, "wb") as f:
        f.write(data)
    print("wrote", OUT)
    print("total size:", len(data))
    validate(OUT)
