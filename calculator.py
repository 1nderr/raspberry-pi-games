import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

btn1 = 4
btn2 = 17
btn3 = 27
btn4 = 22

GPIO.setup(btn1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(btn2, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(btn3, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(btn4, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def calc():
    num1 = float(raw_input("Enter Number One: "))
    num2 = float(raw_input("Enter Number Two: "))
    a = 0
    b = 0
    c = 0
    d = 0
    while True:
        if not GPIO.input(btn1):
            ans = float(num1 + num2)
            print ans
            a = a + 1
            sleep(.3)
            
        elif not GPIO.input(btn2):
            ans =float(num1 - num2)
            print ans
            b = b + 1
            sleep(.3)

            
        elif not GPIO.input(btn3):
            ans = float(num1 * num2)
            print ans
            c = c + 1
            sleep(.3)
            
        elif not GPIO.input(btn4):
            ans = float(num1 / num2)
            print ans
            d = d + 1
            sleep(.3)

        elif a > 0 and b > 0 and c > 0 and d > 0:
            print "\n"
            calc()
try:
    calc()
    
except KeyboardInterrupt:
    GPIO.cleanup()
    
    
