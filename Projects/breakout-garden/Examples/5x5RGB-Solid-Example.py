#!/usr/bin/env python

import time

from rgbmatrix5x5 import RGBMatrix5x5

print("""
RGBMatrix5x5 - Set All Pixels Demo
Uses `set_all` to display solid colours.
Press Ctrl+C to exit!
""")

rgbmatrix5x5 = RGBMatrix5x5()

rgbmatrix5x5.set_clear_on_exit()
rgbmatrix5x5.set_brightness(0.8)

colours = [
    (0xff, 0x00, 0x00),
    (0x00, 0xff, 0x00),
    (0x00, 0x00, 0xff)
]

while True:
    r, g, b = colours.pop(0)
    colours.append((r, g, b))
    rgbmatrix5x5.set_all(r, g, b)
    rgbmatrix5x5.show()
    time.sleep(0.5)

### OR ###

import time
from pimoroni_i2c import PimoroniI2C
from breakout_rgbmatrix5x5 import BreakoutRGBMatrix5x5

PINS_BREAKOUT_GARDEN = {"sda": 4, "scl": 5}
PINS_PICO_EXPLORER = {"sda": 20, "scl": 21}

i2c = PimoroniI2C(**PINS_BREAKOUT_GARDEN)
matrix = BreakoutRGBMatrix5x5(i2c)

colors = []
colors.append((255, 0, 0))
colors.append((0, 255, 0))
colors.append((0, 0, 255))
colors.append((128, 128, 128))

x = 0
y = 0
col = 0

while True:
    matrix.set_pixel(x, y, colors[col][0], colors[col][1], colors[col][2])
    matrix.update()

    x += 1
    if x >= matrix.WIDTH:
        x = 0
        y += 1
        if y >= matrix.HEIGHT:
            y = 0
            col += 1
            if col >= len(colors):
                col = 0
            time.sleep(0.5)

    time.sleep(0.01)
