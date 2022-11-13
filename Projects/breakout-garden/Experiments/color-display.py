#!/usr/bin/env python

# https://github.com/pimoroni/bh1745-python
# https://github.com/pimoroni/rgbmatrix5x5-python
# Useful: https://github.com/pimoroni/pimoroni-pico/blob/main/micropython/examples/pico_explorer/weatherstation_BME280.py

import time
import pimoroni_i2c
import breakout_bh1745
from breakout_rgbmatrix5x5 import BreakoutRGBMatrix5x5

#PINS_BREAKOUT_GARDEN = {"sda": 4, "scl": 5}
PINS_PICO_EXPLORER = {"sda": 20, "scl": 21}

I2C = pimoroni_i2c.PimoroniI2C(**PINS_PICO_EXPLORER)

bh1745 = breakout_bh1745.BreakoutBH1745(I2C, address=0x38)
bh1745.leds(True)

matrix = BreakoutRGBMatrix5x5(I2C, address=0x74)

colours = [
    (0xff, 0x00, 0x00),
    (0x00, 0xff, 0x00),
    (0x00, 0x00, 0xff)
]

colors = []
colors.append((255, 0, 0))
colors.append((0, 255, 0))
colors.append((0, 0, 255))
colors.append((128, 128, 128))

x = 0
y = 0
col = 0

time.sleep(1.0)  # Skip the reading that happened before the LEDs were enabled

try:
    while True:
        #r, g, b = colours.pop(0)
        rgbc_raw = bh1745.rgbc_raw()
        rgb_clamped = bh1745.rgbc_clamped()
        rgb_scaled = bh1745.rgbc_scaled()
        print("Raw: {}, {}, {}, {}".format(*rgbc_raw))
        print("Clamped: {}, {}, {}, {}".format(*rgb_clamped))
        print("Scaled: #{:02x}{:02x}{:02x}".format(*rgb_scaled))
        
        print("Hex: 0x{:02x} 0x{:02x} 0x{:02x}".format(*rgb_scaled))
        
        r, g, b, lum = bh1745.rgbc_clamped()

        #colours.append((r, g, b))
        #matrix.set_all(r, g, b)
        #matrix.set_pixel(x, y, colors[col][0], colors[col][1], colors[col][2])
        matrix.set_pixel(x, y, r, g, b)
        
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
                
        time.sleep(0.01)

        #matrix.set_pixel(1,1,*rgb_clamped[0],*rgb_clamped[1],*rgb_clamped[2])
        #matrix.update()
        time.sleep(0.5)

except KeyboardInterrupt:
    bh1745.set_leds(0)



#from breakout_bme280 import BreakoutBME280
#from pimoroni_i2c import PimoroniI2C
#from pimoroni import PICO_EXPLORER_I2C_PINS
#from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER

# set up the hardware
#display = PicoGraphics(display=DISPLAY_PICO_EXPLORER)
#i2c = PimoroniI2C(**PICO_EXPLORER_I2C_PINS)
#bme = BreakoutBME280(i2c, address=0x76)