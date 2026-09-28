# SOTW HUD Unlock

**Version 2.2.0**

This mod shows three HUD elements in Skyrim Special Edition:

- the compass
- the sneak meter (the eye and the HIDDEN / DETECTED text)
- the crosshair

## Build

1. Run `python tools/build_perkmod.py`. The script writes the file
   `SOTW_HUDUnlock.esp` in the repository root. This file is a build
   output. It is not in this repository.
2. Run `python tools/package_zip.py`. The script writes the file
   `SOTW HUD Unlock-2.2.0.zip` in the parent folder. This file is the
   package for Vortex.

## Requirements

- Skyrim Special Edition
- Skills of the Wild (SOTW) version 2.18 or later
- SOTW Immersive HUD SKSE Patch version 2.17b or later
- ImmersiveHUD SKSE version 3.2.2 or later

## The problem

In SOTW, two skills control two HUD elements:

- Spatial Awareness controls the compass.
- Sixth Sense controls the sneak meter.

You must buy these skills in the game. The SOTW Immersive HUD SKSE Patch
locks the compass and the sneak meter in ImmersiveHUD. ImmersiveHUD hides
a locked element.

ImmersiveHUD also has the "Contextual Crosshair" function. This function
shows the crosshair only when you aim a bow, aim a spell, or look at an
object. In all other moments, the crosshair is hidden.

## The solution

This mod does three things:

1. It sets the two skill ranks to 1. The game thinks that you own both skills.
2. It sets the two ImmersiveHUD locks to 0. ImmersiveHUD can show the
   compass and the sneak meter.
3. It turns off the Contextual Crosshair function. The crosshair shows
   when the HUD shows.

The mod has one plugin and one settings file:

| File | Purpose |
| --- | --- |
| `SOTW_HUDUnlock.esp` | The plugin. It has four global variables. It has no scripts. |
| `MCM\Settings\ImmersiveHUD.ini` | The ImmersiveHUD user settings file. One value turns the Contextual Crosshair function off: `[Crosshair] bEnabled = 0`. |

ImmersiveHUD reads its default settings file first and this user settings
file after it. The user settings file wins. No other mod contains this
file. Therefore no file conflict occurs.

## Installation (Vortex)

1. Close Skyrim.
2. Start Vortex.
3. Click "Mods".
4. If the mod list contains an older version of this mod ("SOTW Compass
   and Sneak Perks" or "SOTW HUD Unlock"), remove it.
5. Click "Install From File".
6. Select the file `SOTW HUD Unlock-2.2.0.zip`.
7. Click "Enable".
8. Click "Deploy Mods".
9. Start Skyrim.

## What you see in the game

- The compass shows with the HUD (new game).
- The sneak meter shows when you sneak (new game). The text HIDDEN or
  DETECTED shows when your detection state changes.
- The crosshair shows when the HUD shows. If you hide the HUD, the
  crosshair hides too.
- The skill menu shows Spatial Awareness and Sixth Sense as owned (new
  game). You do not have to buy them.

## New game and existing saves

- The crosshair fix comes from a settings file. It works in a new game
  and in an existing save.
- The compass and the sneak meter come from plugin values. These values
  apply to a new game only. An existing save keeps its own values for
  these two elements. Skyrim stores the values of all global variables in
  each save file. The game applies the stored values when it loads the
  save. A plugin cannot change them in an existing save.
- This mod does not change your save files.
- Note: a player who wants to change these values in an existing save can
  open the console (the `~` key) and type these commands. This is not
  necessary for a new game.

```
set iHUD_DisableCompass to 0
set iHUD_DisableSneak to 0
set _WWW_PerkRank_SpatialAwareness to 1
set _WWW_PerkRank_SixthSense to 1
```

## Words

- **console**: the command line in the game. Press the `~` key to open it.
- **crosshair**: the small mark in the center of the screen. You use it to aim.
- **global variable**: a value in a plugin. Other plugins and scripts can read it.
- **HUD**: head-up display. The compass, the bars, and the crosshair are HUD elements.
- **MCM**: the settings menu of a mod.
- **plugin**: a file with the extension `.esp`. Skyrim loads plugins.
- **SKSE**: Skyrim Script Extender.

## Files in this repository

- `MCM/Settings/ImmersiveHUD.ini` - the ImmersiveHUD user settings file
- `tools/build_perkmod.py` - the script that builds the plugin
- `tools/package_zip.py` - the script that builds the Vortex package
- `README.txt` - the same text as a plain text file
- `LICENSE` - the license

## Versions

- **2.2.0**: The crosshair fix uses the ImmersiveHUD user settings file.
  No file conflict. The README explains the new game limit of the compass
  and sneak meter fixes.
- **2.1.0**: Show the crosshair. New name and new README.
- **2.0.0**: Show the compass and the sneak meter.

## License

MIT. Read the `LICENSE` file.

## Other mods

Skills of the Wild, ImmersiveHUD SKSE, and the SOTW Immersive HUD SKSE
Patch belong to their authors. This mod only changes values in these mods.
