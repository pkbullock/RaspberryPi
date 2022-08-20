#!/usr/bin/env python3

import time
import math
import sys
from mappings import *
from mappings import custom_controller_mappings

"""
An advanced example of how Trilobot can be remote controlled using a controller or gamepad.
This will require one of the supported controllers to already be paired to your Trilobot.

At startup a list of supported controllers will be shown, with you being asked to select one.
The program will then attempt to connect to the controller, and if successful Trilobot's
underlights will illuminate with a rainbow pattern.

If your controller becomes disconnected Trilobot will stop moving and show a slow red
pulsing animation on its underlights. Simply reconnect your controller and after 10 to 20
seconds, the program should find your controller again and start up again.

This is highly customised to the 8BitDo Zero 2

Press CTRL + C to exit.
"""
print("Trilobot Example: Remote Control\n")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

tbot = Trilobot()

# Presents the user with an option of what controller to use
controller = custom_controller_mappings.choose_controller(0)

# Attempt to connect to the created controller
controller.connect()

# Run an amination on the underlights to show a controller has been selected
for led in range(NUM_UNDERLIGHTS):
    tbot.clear_underlighting(show=False)
    tbot.set_underlight(led, RED)
    time.sleep(0.1)
    tbot.clear_underlighting(show=False)
    tbot.set_underlight(led, GREEN)
    time.sleep(0.1)
    tbot.clear_underlighting(show=False)
    tbot.set_underlight(led, BLUE)
    time.sleep(0.1)

tbot.clear_underlighting()

h = 0
v = 0
spacing = 1.0 / NUM_UNDERLIGHTS

tank_steer = False
underlighting_on = True

# The main loop
while True:
    
    try:

        if not controller.is_connected():
            # Attempt to reconnect to the controller if 10 seconds have passed since the last attempt
            controller.reconnect(10, True)

        try:
            # Get the latest information from the controller. This will throw a RuntimeError if the controller connection is lost
            controller.update()
        except RuntimeError:
            # Lost contact with the controller, so disable the motors to stop Trilobot if it was moving
            tbot.disable_motors()

        if controller.is_connected():

            # Read the controller bumpers to see if the tank steer mode has been enabled or disabled
            try:
                if controller.read_button("L1") and tank_steer:
                    tank_steer = False
                    print("Tank Steering Disabled")
                if controller.read_button("R1") and not tank_steer:
                    tank_steer = True
                    print("Tank Steering Enabled")
            except ValueError:
                # Cannot find 'L1' or 'R1' on this controller
                print("Tank Steering Not Available")

            try:
                if tank_steer:
                    # Have the left stick's Y axis control the left motor, and the right stick's Y axis control the right motor
                    ly = controller.read_axis("LY")
                    ry = controller.read_axis("RY")
                    
                    print("Tank Steer LY:", round(ly), "RY:", round(ry)) 
                    
                    tbot.set_left_speed(-ly)
                    tbot.set_right_speed(-ry)
                    
                else:
                    # Have the left stick control both motors
                    # Up RY = 2.984/3
                    # Idle RY = -509.016/-509
                    # Down RY = -1021.00/-1021
                    
                    # Idle LY = 515.031/515
                    # Left LY = -1/-1
                    # Right = 1031.047/1031
                    ly = round(controller.read_axis("LY"))
                    ry = round(controller.read_axis("RY"))
                    
                    if ly == -509 and ry == 515:
                        print("Stopped")
                        tbot.set_left_speed(0)
                        tbot.set_right_speed(0)
                        tbot.disable_motors()
                    
                    # Forward
                    if ry == 3:
                        print("Forward")
                        tbot.set_left_speed(1)
                        tbot.set_right_speed(1)
                        
                    # Backward
                    if ry == -1021:
                        print("Backward")
                        tbot.set_left_speed(-1)
                        tbot.set_right_speed(-1)
                    
                    # Left
                    if ly == -1:
                        print("Left")
                        tbot.set_left_speed(1)
                        tbot.set_right_speed(-1)
                    
                    # Right
                    if ly == 1031:
                        print("Right")
                        tbot.set_left_speed(-1)
                        tbot.set_right_speed(1)
                                   
            except ValueError:
                # Cannot find 'LX', 'LY', or 'RY' on this controller
                tbot.disable_motors()
                print("Tank steer value error")

            if controller.read_button("Y"):
                tbot.disable_motors()
                tbot.set_left_speed(0)
                tbot.set_right_speed(0)
            
            if controller.read_button("X"):
                if underlighting_on:
                    underlighting_on = False
                else:
                    underlighting_on = True
                time.sleep(0.2)

            # Run a rotating rainbow effect on the RGB underlights
            for led in range(NUM_UNDERLIGHTS):
                led_h = h + (led * spacing)
                if led_h >= 1.0:
                    led_h -= 1.0

                try:
                    if controller.read_button("A"):
                        tbot.set_underlight_hsv(led, 0.0, 0.0, 0.7, show=False)
                    else:
                        tbot.set_underlight_hsv(led, led_h, show=False)
                except ValueError:
                    # Cannot find 'A' on this controller
                    tbot.set_underlight_hsv(led, led_h, show=False)

            if underlighting_on:
                tbot.show_underlighting()
            else:
                tbot.clear_underlighting()

            # Advance the rotating rainbow effect
            h += 0.5 / 360
            if h >= 1.0:
                h -= 1.0

        else:
            # Run a slow red pulsing animation to show there is no controller connected
            val = (math.sin(v) / 2.0) + 0.5
            tbot.fill_underlighting(val * 127, 0, 0)
            v += math.pi / 200

        time.sleep(0.01)
        
    # Exit cleanly
    except KeyboardInterrupt:
        sys.exit(0)
