#import GPIO module and PiSlice module

import RPi.GPIO as GPIO
import PiSlice

#start up 7 segment display

PiSlice.init()

num = 0

while True:
    button = GPIO.input(14)
    while button == 0:
        button = GPIO.input(14)
    while button == 1:
        button = GPIO.input(14)
    num = num + 1
    PiSlice.number = num
