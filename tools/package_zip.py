#!/usr/bin/env python3
"""Build the Vortex package for SOTW HUD Unlock.

The script reads the files of the mod and writes the versioned zip file
in the parent folder of this repository. The zip is a build output.
It is not in this repository.

The zip has only the plugin and the settings file. The README and the
license stay in this repository and on the release page. This keeps the
package free of file conflicts with other mods.

Usage:
    python tools/package_zip.py [output_path]
"""

import os
import sys
import zipfile

VERSION = "2.2.1"

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = (sys.argv[1] if len(sys.argv) > 1
       else os.path.join(os.path.dirname(ROOT), "SOTW HUD Unlock-%s.zip" % VERSION))

# (source in this repository, path in the zip)
FILES = [
    ("SOTW_HUDUnlock.esp", "SOTW_HUDUnlock.esp"),
    ("MCM/Settings/ImmersiveHUD.ini", "MCM/Settings/ImmersiveHUD.ini"),
]


def main():
    missing = [src for src, _ in FILES
               if not os.path.isfile(os.path.join(ROOT, src.replace("/", os.sep)))]
    if missing:
        for f in missing:
            print("missing file:", f)
        print("run tools/build_perkmod.py first")
        sys.exit(1)
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        for src, arc in FILES:
            z.write(os.path.join(ROOT, src.replace("/", os.sep)), arc)
    print("wrote", OUT)
    with zipfile.ZipFile(OUT) as z:
        for info in z.infolist():
            print("  %s (%d bytes)" % (info.filename, info.file_size))


if __name__ == "__main__":
    main()
