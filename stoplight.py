import RPi.GPIO as GPIO
from time import sleep
from sys import exit

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
OUT = GPIO.OUT

grn = int(raw_input("Green light GPIO pin: "))
ylw = int(raw_input("Yellow light GPIO pin: "))
red = int(raw_input("Red light GPIO pin: "))

GPIO.setup(grn, OUT)
GPIO.setup(ylw, OUT)
GPIO.setup(red, OUT)

try:
    while True:
        GPIO.output(grn, True)
        sleep(3)
        GPIO.output(grn, False)
        GPIO.output(ylw, True)
        sleep(3)
        GPIO.output(ylw, False)
        GPIO.output(red, True)
        sleep(3)
        GPIO.output(red, False)
        
except KeyboardInterrupt:
    print "Clearing GPIO pins and exiting."
    GPIO.output(grn, False)
    GPIO.output(ylw, False)
    GPIO.output(red, False)
    GPIO.cleanup()
    exit(0)
