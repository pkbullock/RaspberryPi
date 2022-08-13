#!/usr/bin/env python3

import ST7735
import sys

st7735 = ST7735.ST7735(
    port=0,
    cs=1,
    dc=9,
    backlight=12,
    rotation=270,
    spi_speed_hz=10000000
)

# Reset the display
st7735.begin()
st7735.reset()
st7735.set_backlight(0)

print("\nDone.")  

# Exit cleanly
sys.exit(0)
