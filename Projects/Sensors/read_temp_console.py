#!/usr/bin/python

# Project requires the following library to run:
# 	https://github.com/adafruit/Adafruit_Python_DHT


import sys
import Adafruit_DHT

try:
	while True:
		humidity, temperature = Adafruit_DHT.read_retry(11, 4)
		print 'Temp: {0:0.1f} C Humidity: {1:0.1f} % '.format(temperature, humidity)

except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C  

    print "\nProgram Ended."  
  
except:  
    # this catches ALL other exceptions including errors.  
    # You won't get any error messages for debugging  
    # so only use it once your code is working  

    print "Other error or exception occurred!" 

	