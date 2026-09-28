# SOTW HUD Unlock

**Version 2.1.0**

This mod shows three HUD elements in Skyrim Special Edition:

- the compass
- the sneak meter (the eye and the HIDDEN / DETECTED text)
- the crosshair

## Build

Run `python tools/build_perkmod.py`. The script writes the file
`SOTW_HUDUnlock.esp` in the repository root. This file is a build output.
It is not in this repository.

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
| `MCM\Config\ImmersiveHUD\settings.ini` | The ImmersiveHUD settings file. One value is different: `[Crosshair] bEnabled = 0`. |

## Installation (Vortex)

1. Close Skyrim.
2. Start Vortex.
3. Click "Mods".
4. Click "Install From File".
5. Select the file `SOTW HUD Unlock-2.1.0.zip`.
6. Click "Enable".
7. Click "Deploy Mods".
8. If Vortex shows a file conflict for the file `settings.ini`, set
   SOTW HUD Unlock to win the conflict. Two mods contain this file:
   ImmersiveHUD SKSE and SOTW HUD Unlock.
9. Start Skyrim.

If the file conflict stays unresolved, the Contextual Crosshair function
stays on. You can turn it off in the game:

1. Open the ImmersiveHUD MCM.
2. Open the "General" page.
3. Turn off "Contextual Crosshair".

## New game or old save

- A new game reads the plugin values. The elements show immediately.
- An old save keeps its own values. If the elements stay hidden, open the
  console and type these commands:

```
set iHUD_DisableCompass to 0
set iHUD_DisableSneak to 0
set _WWW_PerkRank_SpatialAwareness to 1
set _WWW_PerkRank_SixthSense to 1
```

## What you see in the game

- The compass shows with the HUD.
- The sneak meter shows when you sneak. The text HIDDEN or DETECTED shows
  when your detection state changes.
- The crosshair shows when the HUD shows. If you hide the HUD, the
  crosshair hides too.
- The skill menu shows Spatial Awareness and Sixth Sense as owned. You do
  not have to buy them.

## Words

- **crosshair**: the small mark in the center of the screen. You use it to aim.
- **global variable**: a value in a plugin. Other plugins and scripts can read it.
- **HUD**: head-up display. The compass, the bars, and the crosshair are HUD elements.
- **MCM**: the settings menu of a mod.
- **plugin**: a file with the extension `.esp`. Skyrim loads plugins.
- **SKSE**: Skyrim Script Extender.

## Files in this repository

- `MCM/Config/ImmersiveHUD/settings.ini` - the ImmersiveHUD settings file
- `tools/build_perkmod.py` - the script that builds the plugin
- `README.txt` - the same text as a plain text file
- `LICENSE` - the license

## Versions

- **2.1.0**: Show the crosshair. New name and new README.
- **2.0.0**: Show the compass and the sneak meter.

## License

MIT. Read the `LICENSE` file.

## Other mods

Skills of the Wild, ImmersiveHUD SKSE, and the SOTW Immersive HUD SKSE
Patch belong to their authors. This mod only changes values in these mods.
