#!/user/bin/python
'''
    led.py
    ~~~~~~~~~~~~~~~~
    led warning  module.
    :copyright: (c) 2017 by jxg.
'''
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

def led(t):         #灯闪烁
    for i in range(0,t):
        GPIO.output(11,False)
        time.sleep(0.25)
        GPIO.output(11,True)
        time.sleep(0.75)

def led_on():       #开灯
    GPIO.output(11,True)

def led_off():      #关灯
    GPIO.output(11,False)
