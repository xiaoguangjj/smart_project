#!/user/bin/python

import RPi.GPIO as GPIO
import time

<<<<<<< HEAD
def buzz(buzztime):

=======
def buzz():
	buzztime = 5
>>>>>>> 448d98d7f476526340a69fc98490089e6f96e216
	GPIO_PIN = 23;
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(GPIO_PIN,GPIO.OUT);
	GPIO.output(GPIO_PIN,GPIO.LOW);
	time.sleep(buzztime);
	GPIO.output(GPIO_PIN,GPIO.HIGH);
	GPIO.cleanup();

