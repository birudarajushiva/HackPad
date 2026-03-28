import board
import busio
import displayio
import terminalio
import adafruit_displayio_ssd1306
from adafruit_display_text import label
import rotaryio
import keypad
import usb_hid
from adafruit_hid.keyboard import Keyboard
from config import BUTTON_MAP, DIAL_CLOCKWISE, DIAL_COUNTER, STARTUP_MESSAGE

displayio.release_displays()
i2c = busio.I2C(board.D5, board.D4)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)
splash = displayio.Group()
display.show(splash)
text_area = label.Label(terminalio.FONT, text=STARTUP_MESSAGE, color=0xFFFFFF, x=5, y=15)
splash.append(text_area)

keyboard = Keyboard(usb_hid.devices)
keys = keypad.KeyMatrix(
    row_pins=(board.D0, board.D1),
    column_pins=(board.D2, board.D3, board.D4, board.D5),
)
encoder = rotaryio.IncrementalEncoder(board.D6, board.D7)
last_position = encoder.position

while True:
    event = keys.events.get()
    if event:
        button = event.key_number
        if event.pressed and button in BUTTON_MAP:
            keyboard.press(*BUTTON_MAP[button]["keys"])
            text_area.text = BUTTON_MAP[button]["name"]
        if event.released:
            keyboard.release_all()
            text_area.text = STARTUP_MESSAGE

    current_position = encoder.position
    if current_position != last_position:
        if current_position > last_position:
            keyboard.press(*DIAL_CLOCKWISE["keys"])
            keyboard.release_all()
            text_area.text = DIAL_CLOCKWISE["name"]
        else:
            keyboard.press(*DIAL_COUNTER["keys"])
            keyboard.release_all()
            text_area.text = DIAL_COUNTER["name"]
        last_position = current_position
