#!/usr/bin/env python2.7

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)


but_led_left = 17
but_led_right = 18

but_right = 22
but_left = 27

GPIO.setup(but_right, GPIO.IN)
GPIO.setup(but_left, GPIO.IN)

rdy_led = 19
flt_led = 26

beacon_led = 13
blue_led = 6

time_stamp = time.time()

def bounce():
    global time_stamp
    time_now = time.time()  
    if (time_now - time_stamp) >= 0.3:
        time_stamp = time.time()
        return False
    return True

def onLeftButton(channel):
    if not bounce():
        print 'left'

def onRightButton(channel):
    print 'right'


GPIO.add_event_detect(but_right, GPIO.RISING, callback=onRightButton)
GPIO.add_event_detect(but_left, GPIO.RISING, callback=onLeftButton)

try:
    while True:
        time.sleep(4)
except:
    pass
finally:
    GPIO.cleanup()

print 'exiting'
