# HackPad
### A programmable macropad, from PCB to enclosure to firmware

An eight-key macropad design with an EC11 rotary encoder and a 128×32 SSD1306 OLED, built around the Seeed Studio XIAO RP2040 for Hack Club's Blueprint mission.

This repository brings together the KiCad board and schematic, manufacturing exports, enclosure CAD, and CircuitPython firmware. **Treat it as a hardware prototype: the committed firmware needs the issues below resolved before a complete working build can be claimed.**

## Explore the design

- [PCB layout](PCB/Hackpad.kicad_pcb) and [schematic](PCB/Hackpad.kicad_sch): editable KiCad source.
- [Gerber archive](PCB/gerbers.zip): fabrication export; review against the source before ordering.
- [Enclosure source](CAD/SmartOledbyShiva.step): editable STEP assembly.
- [Top](CAD/Oledtoptray.stl) and [bottom](CAD/Oledbottomtray.stl): printable enclosure meshes; physical fit requires verification.
- [Firmware](firmware/main.py) and [shortcut configuration](firmware/config.py).
- [Design screenshots](images/) and [bill of materials](BOM.csv).

## Intended interaction

The default mappings are Copy, Paste, Undo, Save, Cut, Select All, Switch, and Close. The display shows the selected action; the encoder is intended to control volume. Mappings live in `firmware/config.py`.

## Hardware and assembly

The design uses a XIAO RP2040, eight Cherry MX switches and keycaps, an EC11 encoder, an SSD1306 I²C OLED, matrix diodes, and M3 hardware. The historical BOM includes tooling and example supplier prices; it is not a current purchase quote. Its diode quantities differ from the original prose, so reconcile them with the schematic.

Before fabrication, run KiCad electrical/design-rule checks, confirm footprints and pin assignments, and compare the Gerbers with the board. Review the enclosure dimensions before printing, then solder and inspect the assembly before applying USB power.

## Firmware status and blockers

Static inspection of the committed source found:

- **Pin conflict:** D4/D5 are assigned to both OLED I²C and the key matrix. Resolve the pinout against the schematic before wiring or powering a build.
- **Volume handling:** the configuration uses `Keycode.VOLUME_INCREMENT` and `Keycode.VOLUME_DECREMENT` through a keyboard HID object. Verify the library API and implement Consumer Control HID for volume.
- **Runtime compatibility:** display initialization uses `displayio.I2CDisplay` and `display.show`; check compatibility with the selected CircuitPython release.

After those issues are resolved, install a compatible CircuitPython release on the XIAO RP2040. Copy the HID, display-text, and SSD1306 display libraries and their dependencies to `CIRCUITPY/lib/`. Copy `firmware/config.py` to `CIRCUITPY/config.py` and `firmware/main.py` to `CIRCUITPY/code.py` so it starts automatically.

Validate startup, all eight key positions, press/release behavior, simultaneous keys, both encoder directions, and OLED feedback on the actual board. This documentation update does not claim those hardware checks have passed.

## Reuse

No repository-wide license is currently included. Confirm reuse permission before redistributing the design.
