# Pin ownership audit

The current firmware contains a source-level overlap: the OLED I²C bus claims
D5/D4 at line 14, and the key matrix claims them again at line 23.

This was reproduced using [CircuitPython Pin Audit](https://github.com/birudarajushiva/circuitpython-pin-audit)
at commit `ae455d5d4887373d2b33d7c72b2c6c52c99b5098`, against
[`firmware/main.py`](../firmware/main.py) from HackPad commit
`8ebea2cc15d34a8ab294d87b1208da995ef5eafb`.

## Reproduce

In a local Python 3.10+ virtual environment, from the HackPad repository root:

```sh
python -m pip install 'git+https://github.com/birudarajushiva/circuitpython-pin-audit.git@ae455d5d4887373d2b33d7c72b2c6c52c99b5098'
pin-audit firmware/main.py
```

Expected diagnostics for that exact firmware:

```text
firmware/main.py:23:8: PA001 Potential overlap on board.D4: keypad.KeyMatrix (column_pins) and busio.I2C (sda, line 14).
firmware/main.py:23:8: PA001 Potential overlap on board.D5: keypad.KeyMatrix (column_pins) and busio.I2C (scl, line 14).
```

The command exits 1 and reports three supported allocations (I²C, key matrix,
encoder), with two potential conflicts. It parses source without importing
CircuitPython, running firmware, or connecting to hardware.

## What a repair must establish

Compare the firmware assignments with the KiCad schematic, PCB routing, and
actual assembly. Select a physically valid pin arrangement; a symbolic free pin
is not enough if the manufactured board connects the signals differently.
Update wiring/PCB and firmware together when required.

Rerun the checker, then test all keys, both encoder directions, OLED feedback,
and key release behavior on the real board. The separate Consumer Control HID
and display-runtime issues in the main README still require attention.

This audit does not change pin assignments, certify electrical correctness, or
claim a working hardware build. The checker's supported constructors and
[analysis limits](https://github.com/birudarajushiva/circuitpython-pin-audit/blob/ae455d5d4887373d2b33d7c72b2c6c52c99b5098/docs/limitations.md)
must be considered before making it a required CI check.
