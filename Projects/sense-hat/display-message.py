#!/usr/bin/python

from time import sleep
from sense_hat import SenseHat

sense = SenseHat()

try:

    # Examples
    # More examples can be found at: https://www.raspberrypi.org/learning/getting-started-with-the-sense-hat/worksheet/
    
    #sense.show_message("Hello, my name is HAL")
    
    sense.show_message("Hello, my name is HAL", scroll_speed=0.05, text_colour=[255,255,0])

    

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