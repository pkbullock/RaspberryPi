#!/usr/bin/env python

# https://github.com/pimoroni/bh1745-python

import time
from bh1745 import BH1745

bh1745 = BH1745()

bh1745.setup()
bh1745.set_leds(1)

time.sleep(1.0)  # Skip the reading that happened before the LEDs were enabled

try:
    while True:
        r, g, b = bh1745.get_rgb_scaled()
        print('#{:02x}{:02x}{:02x}'.format(r, g, b))
        time.sleep(0.5)

except KeyboardInterrupt:
    bh1745.set_leds(0)

### OR ###

import time

import pimoroni_i2c
import breakout_bh1745

PINS_BREAKOUT_GARDEN = {"sda": 4, "scl": 5}
PINS_PICO_EXPLORER = {"sda": 20, "scl": 21}

I2C = pimoroni_i2c.PimoroniI2C(**PINS_BREAKOUT_GARDEN)
bh1745 = breakout_bh1745.BreakoutBH1745(I2C)

bh1745.leds(True)

while True:
    rgbc_raw = bh1745.rgbc_raw()
    rgb_clamped = bh1745.rgbc_clamped()
    rgb_scaled = bh1745.rgbc_scaled()
    print("Raw: {}, {}, {}, {}".format(*rgbc_raw))
    print("Clamped: {}, {}, {}, {}".format(*rgb_clamped))
    print("Scaled: #{:02x}{:02x}{:02x}".format(*rgb_scaled))
    time.sleep(5)
