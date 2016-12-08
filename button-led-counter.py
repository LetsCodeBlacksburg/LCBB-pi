#import GPIO module and PiSlice module
import RPi.GPIO as GPIO
import PiSlice 	#load module
#DIO=13, SCLK=11, RCLK=12
import time

#start up 7 segment display
PiSlice.init()

num = 0

while True:
  button = GPIO.input(16)
  while button == 0:
    button = GPIO.input(16)
    time.sleep(0.1)   # A timing hack to prevent LED display corruption
  while button == 1:
    button = GPIO.input(16)
    time.sleep(0.1)   # A timing hack to prevent LED display corruption
  num = num + 1
  PiSlice.number = num
