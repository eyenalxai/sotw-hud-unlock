SOTW HUD Unlock
Version 2.2.1

This mod shows three HUD elements in Skyrim Special Edition. They are
the compass, the sneak meter and the crosshair.

Skills of the Wild hides the compass and the sneak meter until you learn
two skills. ImmersiveHUD hides the crosshair until you aim. This mod
removes both limits.

REQUIREMENTS
- Skyrim Special Edition
- Skills of the Wild 2.18 or later
- SOTW Immersive HUD SKSE Patch 2.17b or later
- ImmersiveHUD SKSE 3.2.2 or later

INSTALL
1. Close Skyrim.
2. Open Vortex and click Mods.
3. Remove an old version of this mod if it is in the list.
4. Click Install From File and select the zip file.
5. Click Enable and then Deploy Mods.
6. Start Skyrim.

If Vortex shows a file conflict for MCM/Settings/ImmersiveHUD.ini, set
SOTW HUD Unlock as the winner for that file. The crosshair fix needs our
copy.

NEW GAME AND EXISTING SAVES
The crosshair fix works in a new game and in an existing save.

The compass and the sneak meter fixes work in a new game only. An
existing save keeps its own values for these two elements. Skyrim stores
these values inside each save file. The mod does not change your save
files.

BUILD
Run "python tools/build_perkmod.py" to build the plugin.
Run "python tools/package_zip.py" to build the zip.

LICENSE
MIT. Read the LICENSE file.
