#!/usr/bin/env python2.7

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)


but_led_left = 17
but_led_right = 18

but_right = 22
but_left = 27

rdy_led = 19
flt_led = 26

beacon_led = 13
blue_led = 6


def onLeftButton(channel):
    pass

def onRightButton(channel):
    pass


GPIO.add_event_detect(but_right, GPIO.RISING, callback=onRightButton)
GPIO.add_event_detect(but_left, GPIO.RISING, callback=onLeftButton)

try:
    while True:
        time.sleep(4)
finally:
    GPIO.cleanup()

print 'exiting'
