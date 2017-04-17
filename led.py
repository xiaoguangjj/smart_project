#!/user/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

def led(t):
	for i in range(0,t):
		GPIO.output(11,True)
		time.sleep(0.25)
		GPIO.output(11,False)
		time.sleep(0.75)
