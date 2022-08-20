# Macro Keyboard

This Repository is for the Software of the Macro Keyboard developed by [Meiiikum](https://github.com/Meiiikum) and [ScheerleJo](https://github.com/ScheerleJo). The Hardware Components and 3d-Models is on Thingiverse (Link Coming soon). It will look something like this:

![Design](img/design.png)

The Plan is to 3d-Print everything possible including the Enclosure, Keycaps, Encoder-Wheels and so on.

## Aim

The Aim of this project is to

- get better at 3d Modelling and sharpen coding skills
- but more important to simplify and speed up various tasks. From Editing Videos to writing Code or possibly even Gaming shall be all included

## Plans

The Keyboard will have multiple Layers for the different applications of usage for it.
A few functions will be the same over the different Layers such as:

- Open pograms like the Adobe Creative Cloud / Gimp /
- Implement 3 or 4 different clipboards to store different contents and paste them directly when previously imported in one of the clipboard banks.

### TODO

- Py-Lib Requests need global environment
- Host html/php-site with pyton script for Debugging
  - End-Points and test scripts
    - see current keyboard layer & and functions
    - check Status of Arduino (COM-Port, Latest Button press)
    - Oversee status of End-Point-Scripts like CEP, HotkeylessAHK

### Global functions

The following functions will be available independant from the current Layer (e.g. A1-B5)

- [ ] Key Lock
- [ ] Undo
- [ ] Redo
- [ ] Reset Arduino (-> if pressed: arduino and all running scripts are rebooted)
- [ ] Windows Key
- [ ] keyboard Lock (from normal Keyboard)
- [ ] Start several Programs
  - Premiere
  - Photoshop / Gimp
  - After Effects
  - Spotify
  - Task Manager

### Editing Layer

This Layer will have the ability to access the Premiere CEP interface to speed up and Control important funtions.

- [ ] stabilization has to be implemented
- [ ] 16:9 sizer
- [ ] save project as (Sicherheitskopie)
- [ ] zoom out to see the whole project in the timeline
- [ ] Zoom in/out on selected clip
- [ ] Crop in/out by 20% is not possible
- [ ] gauisian blur
- [ ] Drop shadow
- [ ] Lumetri color window opens
- [ ] lumetri Color Encoder
- [ ] Switch audio channels to left only
- [ ] Switch audio channels to right only
- [ ] lowers the volume by 3db of selected clip (relative)
- [ ] raises the volume by 3db of selected clip (relative)
- [ ] mute selected clip
- [ ] run screenshottool
- [ ] opening Programs next to the numpad
- [ ] jump to marker (1-10) & next/previous Marker
- [ ] color selected CLips in color a/b/c/d
- [ ] disable all applied effecs on all selected clips
- [ ] connect Captions
- [ ] split Captions
- [ ] eddit current Caption
- [ ] MultiCam selection for first 8 Cameras
- [ ] Timeline on an Encoder
- [ ] Export Single Frame as Image
- [ ] Color Key + hue vs. hue in a Lumetri Effect
- [ ] Target single video Tracks

### Utility Layer

That will be the standard Layer, what the Keyboard will boot to by default. When not using for editing or programming, some useful macros and tools shall be available for direct access.

### Programming Layer

The Programming Layer will implement some simple functions for the better development of software on windows.
Some useful functions would be:

- [ ] Open CMD in the current directory
- [ ] Open VSC with the working directory on the current active folder
- [ ] pulling the new code from Github
- [ ] ...

## Current status

Currently there is little progress done. The main task is to model and create the hardware of the Keyboard before it can be fully tested.
Next up is to fully test the software architecture which handles all the communication between the Arduino and the PC-side. Another soon upcoming TODO is starting to test and implement the different functions and communicaation between programming languages in the layers

## Developers

<img src="https://avatars.githubusercontent.com/ScheerleJo"   height="50px" title="Josia Scheerle"/> | [`@ScheerleJo`](https://github.com/ScheerleJo)
<img src="https://avatars.githubusercontent.com/Meiiikum"   height="50px" title="Josia Scheerle"/> | [`@Meiiikum`](https://github.com/Meiiikum)
