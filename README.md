# Ubuntu PCSX2 Handler

Tested with a ps3 sixaxis controller connected via bluetooth, but you should be able to use any controller (as long as pygame recognizes it) by changing  `selectButton` and `startButton`values to your controllers values.



### What does the script do?

It solves the problem of having to use a keyboard to close pcsx2, making it possible to close it with the `start + select` emulationstation friendly button combination.



### Usage

1. Download the script and place it on `/home/$Username/pcsx2_handler`

1. Make it executable: `sudo chmod +x /home/yourusername/pcsx2_handler/pcsx2_handler.py`



At this point you should be able to execute it by opening the terminal and typing:
`/home/yourusername/pcsx2_handler/pcsx2_handler/pcsx2_handler.py --pcsx2 "usr/games/PCSX2 --fullscreen --nogui pathtoyouriso"`

To quit PCSX2 just press start and select button simultaneously.



### Integration on emulationstation

1. Follow the instructions above to place and make the script executable.

1. You must edit `es_system.cfg` to launch the script, in my case it is located on `/home/user/.emulationstation/es_system.cfg`


Add the following to `es_system.cfg` **between** `<systemList>` tags:

```xml
<system>
    <name>ps2</name>
    <fullname>PlayStation 2</fullname>
    <path>pathToYourPs2RomFolder</path>
    <extension>.iso .ISO .cue .CUE</extension>
    <command>/home/yourusername/pcsx2_handler/pcsx2_handler.py  --pcsx2 "/usr/games/PCSX2 --fullscreen --nogui %ROM%"</command>
    <platform>ps2</platform>
    <theme>ps2</theme>
</system>
```


**Restart** emulationstation and you should have the script properly integrated, it will handle the PCSX2 emulator and take you back to emulationstation when you close PCSX2 emulator.

