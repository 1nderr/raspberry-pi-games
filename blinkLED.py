#!/usr/bin/env python

# blinky.py turns on a GPIO pin for 5 seconds then clears.

import RPi.GPIO as GPIO
from time import sleep
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

print "What GPIO pin are you using?"

pinLED = int(raw_input(">>> "))

GPIO.setup(pinLED, GPIO.OUT)
print "GPIO pin %r is ON." % pinLED
GPIO.output(pinLED, True)
sleep(5)
GPIO.cleanup()
print "GPIO pins cleared."
sleep(1)
sys.exit(0)




