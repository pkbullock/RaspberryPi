#!/usr/bin/python

from time import sleep
from sense_hat import SenseHat

sense = SenseHat()

r = [255, 0, 0]     # red
o = [255, 127, 0]   # orange
y = [255, 255, 0]   # yellow
g = [0, 255, 0]     # green
b = [0, 0, 255]     # blue
i = [75, 0, 130]    # indigo
v = [159, 0, 255]   # violet
e = [0, 0, 0]       # none

image = [e, e, e, e, e, e, e, e,
         e, e, e, r, r, e, e, e,
         e, r, r, o, o, r, r, e,
         r, o, o, y, y, o, o, r,
         o, y, y, g, g, y, y, o,
         y, g, g, b, b, g, g, y,
         b, b, b, i, i, b, b, b,
         b, i, i, v, v, i, i, b]

try:

    sense.set_pixels(image)

    while True:
        angles = [0, 90, 180, 270, 0, 90, 180, 270]
        for r in angles:
            sense.set_rotation(r)
            sleep(0.1)

except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C  

    print "\nProgram Ended."  
  
except:  
    # this catches ALL other exceptions including errors.  
    # You won't get any error messages for debugging  
    # so only use it once your code is working  

    print "Other error or exception occurred!" 

finally:
    # Clean up
    sense.clear()