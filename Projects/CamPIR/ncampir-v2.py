import RPi.GPIO as GPIO
import picamera
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN)

#GPIO.setup(18, GPIO.OUT)

camera = picamera.PiCamera()
camera.resolution = (1024, 768)

try:
	while True:
		#GPIO.output(18, True)
		input_state = GPIO.input(17)
		if input_state == True:
			print('Motion Detected')
			
			camera.start_preview()
			time.sleep(2)
			filename = 'night-motion-'+time.strftime('%Y%m%d-%H%M%S')+'.jpg'
			camera.capture(filename)
			time.sleep(2)
			camera.stop_preview()
			print(filename)
finally:
	print('Cleaning Up')
	#GPIO.output(18, False)
	GPIO.cleanup()
	camera.close()