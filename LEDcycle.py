import RPi.GPIO as GPIO
from time import sleep
from sys import exit

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

button = int(raw_input("Button GPIO pin: "))
light1 = int(raw_input("Light 1 GPIO pin: "))
light2 = int(raw_input("Light 2 GPIO pin: "))
light3 = int(raw_input("Light 3 GPIO pin: "))
light4 = int(raw_input("Light 4 GPIO pin: "))

GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(light1, GPIO.OUT)
GPIO.setup(light2, GPIO.OUT)
GPIO.setup(light3, GPIO.OUT)
GPIO.setup(light4, GPIO.OUT)

x = 0

try:
    while True:
        GPIO.output(light1, not GPIO.input(button) and x == 0)
        if not GPIO.input(button) and x == 0:
            sleep(.1)
            x = x + 1
            sleep(.5)
            
        GPIO.output(light2, not GPIO.input(button) and x == 1)
        if not GPIO.input(button) and x == 1:
            sleep(.1)
            x = x + 1
            sleep(.5)
            
        GPIO.output(light3, not GPIO.input(button) and x == 2)
        if not GPIO.input(button) and x == 2:
            sleep(.1)
            x = x + 1
            sleep(.5)
            
        GPIO.output(light4, not GPIO.input(button) and x == 3)
        if not GPIO.input(button) and x == 3:
            sleep(.1)
            x = 0
            sleep(.5)

except KeyboardInterrupt:
    print "Exiting..."
    GPIO.output(light1, False)
    GPIO.output(light2, False)
    GPIO.output(light3, False)
    GPIO.output(light4, False)
    GPIO.cleanup()
    exit(0)

