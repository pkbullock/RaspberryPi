#!/usr/bin/python

from time import sleep
from sense_hat import SenseHat

sense = SenseHat()

try:

    sense.show_message("Hello, my name is HAL")

    

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