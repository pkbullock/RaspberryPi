#!/usr/bin/env python

# import sys
import subprocess
import shlex
from time import sleep

try:
    import blinkt
except ImportError:
    exit("This script requires blinkt module\nInstall with: sudo apt-get install python-blinkt")

# default interface
interface = "wlan0"

# default brightness to low so not to blind the user
blinkt.set_brightness(0.2)
blinkt.set_clear_on_exit(True)

def get_quality(line):

    """Determine signal quality from string"""

    try:

        # print("line " + line)
        # print("sig split" + line.split("Signal level=")[0])
        # print("lq split" + line.split("Signal level=")
        #    [0].split("Link Quality=")[1])

        if line == "":
            return 0

        level = line.split("Signal level=")[0].split("Link Quality=")[1]
        quality = level.split('/')

        if not quality:
            return 0
        else:
            return int(round(float(quality[0]) / float(quality[1]) * 100))

    except:

        print("\nget_quality method error")
        return 0

def display_level(strength):

    """Display a level on the blinkt"""

    # 1/8 the value
    # 3/8 = red rgb(255,0,0)
    # 5/8 = yellow rgb(255,255,0)
    # 8/8 = green rgb(0,255,0)

    # 1.25 is the deciding value
    led_threshold = strength / 1.25
    no_of_leds = round(led_threshold / 10)

    print('Led threshold: ' + str(led_threshold))
    print('No of Leds. ' + str(no_of_leds))

    r, g, b = 0, 0, 0

    if led_threshold <= 30:
        # red
        r = 255
        g = 0
    else:
        if led_threshold <= 50:
            # yellow
            r = 255
            g = 255
        else:
            # green
            r = 0
            g = 255

    print('red:' + str(r))
    print('green:' + str(g))
    print('blue:' + str(b))

    # set all leds
    for i in range(8):
        if no_of_leds > i:
            blinkt.set_pixel(i, r, g, b)
        else:
            blinkt.set_pixel(i, 0, 0, 0)

    blinkt.show()

def display_no_signal():

    """Shows a no signal indication"""
    blinkt.set_all(255, 0, 0) # red

def display_reset():

    """Resets the display to empty"""
    blinkt.set_all(0, 0, 0) # off

def main():

    """Run the main process for this script"""

    try:

        while True:

            proc1 = subprocess.Popen(shlex.split(
                'iwconfig wlan0'), stdout=subprocess.PIPE)
            proc2 = subprocess.Popen(shlex.split('grep "Link Quality"'), stdin=proc1.stdout,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # example output - Link Quality=66/70  Signal level=-44 dBm

            proc1.stdout.close()  # Allow proc1 to receive a SIGPIPE if proc2 exits.
            out, err = proc2.communicate()

            print('out: {0}'.format(out))
            print('err: {0}'.format(err))

            current_strength = get_quality(out)

            # print('strength:' + str(current_strength))

            if current_strength > 0:
                print("Quality: " + str(current_strength).rjust(3) + " %")
                display_level(current_strength)
            else:
                print("No signal!")
                display_no_signal()

            sleep(1) # loop per second

    except KeyboardInterrupt:
        # here you put any code you want to run before the program
        # exits when you press CTRL+C

        print("\nProgram Ended.")

    except:
        # this catches ALL other exceptions including errors.
        # You won't get any error messages for debugging
        # so only use it once your code is working

        print("Other error or exception occurred!")


main()




