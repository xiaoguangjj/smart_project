#!/user/bin/python
# -*- coding: utf8 -*-

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

def led_on():      #turn on light
    GPIO.output(11,False)
