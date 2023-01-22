import argparse
import blinkt
import time
import sys
from threading import Thread
from picamera2 import Picamera2

# Create the parser
parser = argparse.ArgumentParser(description='Take timelapse photos')

# Add the hours parameter
parser.add_argument('--hours', type=int, default=2, help='Number of hours to run the timelapse')

# Parse the command line arguments
args = parser.parse_args()

# Pi Cam Config
picam2 = Picamera2()
picam2.configure("still")
picam2.start()

total_photos = int(args.hours * 60)

path = '/home/pi/Pictures'

# Set the brightness of the LEDs
blinkt.set_brightness(0.1)

# Give time for Aec and Awb to settle, before disabling them
time.sleep(1)
picam2.set_controls({"AeEnable": False, "AwbEnable": False, "FrameRate": 1.0})
# And wait for those settings to take effect
time.sleep(1)

# Calculate the total number of photos based on hours
total_photos = int(hours * 60)

def light_led():
    for i in range(total_photos):
        # Light up the first LED while the picture is being captured
        blinkt.set_pixel(0, 255, 0, 0)
        blinkt.show()
        time.sleep(4)
        # Turn off the first LED
        blinkt.set_pixel(0, 0, 0, 0)
        blinkt.show()
        # Wait for 0.5 seconds before taking the next picture
        time.sleep(0.5)

# Take a photo every minute
for i in range(total_photos):
    # start the thread for the leds
    t1 = Thread(target = light_led)
    t1.start()
    
    # Capture the picture
    r = picam2.capture_request()
    r.save("main", f"tl_photo{str(i)}.jpg")
    r.release()
    print(f"Captured image {i}")
    t1.join()


picam2.stop()
