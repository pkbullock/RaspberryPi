import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN)

GPIO.setup(18, GPIO.OUT)

while True:
	input_state = GPIO.input(17)
	GPIO.output(18, False)
	if input_state == True:
		print('Motion Detected')
		GPIO.output(18, True)
		time.sleep(1)