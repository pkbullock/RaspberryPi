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

# Calculate the total number of photos based on hours
total_photos = int(args.hours * 60)

path = '/home/pi/Pictures'

# Set the brightness of the LEDs
blinkt.set_brightness(0.1)

# Give time for Aec and Awb to settle, before disabling them
time.sleep(1)
picam2.set_controls({"AeEnable": False, "AwbEnable": False, "FrameRate": 1.0, "AfMode": 2, "AfTrigger": 0})
# And wait for those settings to take effect
time.sleep(1)

def light_led():
    for i in range(1,8):
        # Light up the first LED while the picture is being captured
        blinkt.set_pixel(i, 255, 127, 0)
        blinkt.show()
        time.sleep(0.5)

def reset_led():
    blinkt.set_all(0, 0, 0)    
    blinkt.show()
    blinkt.clear()

def main():

     # The main loop
    try:
        while True:
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

                reset_led()
                print(f"Waiting for 60 seconds...")
                time.sleep(60)
     
     # Exit cleanly
    except KeyboardInterrupt:
        print("Exiting...")
        picam2.stop()
        sys.exit(0)

if __name__ == "__main__":
    main()
