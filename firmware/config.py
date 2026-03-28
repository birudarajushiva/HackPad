from adafruit_hid.keycode import Keycode

BUTTON_MAP = {
    0: {"keys": [Keycode.CONTROL, Keycode.C], "name": "Copy"},
    1: {"keys": [Keycode.CONTROL, Keycode.V], "name": "Paste"},
    2: {"keys": [Keycode.CONTROL, Keycode.Z], "name": "Undo"},
    3: {"keys": [Keycode.CONTROL, Keycode.S], "name": "Save"},
    4: {"keys": [Keycode.CONTROL, Keycode.X], "name": "Cut"},
    5: {"keys": [Keycode.CONTROL, Keycode.A], "name": "Select All"},
    6: {"keys": [Keycode.ALT, Keycode.TAB], "name": "Switch"},
    7: {"keys": [Keycode.CONTROL, Keycode.W], "name": "Close"},
}
DIAL_CLOCKWISE = {"keys": [Keycode.VOLUME_INCREMENT], "name": "Vol UP"}
DIAL_COUNTER = {"keys": [Keycode.VOLUME_DECREMENT], "name": "Vol DOWN"}
STARTUP_MESSAGE = "Shiva's Pad!"
