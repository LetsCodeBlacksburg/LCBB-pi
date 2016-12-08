#import GPIO module
 import RPi.GPIO as GPIO
 #import time for sleep function
 import time  
#initialize GPIO to use Raspberry Pi pinouts 
GPIO.setmode(GPIO.BOARD)
 #set pin 15 to output mode and 16 to input
 GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.IN)
while True:
    button = GPIO.input(16)
    while button == True:
        print 'waiting'
        button = GPIO.input(16)
     #turn on LED and wait 1 second 
    GPIO.output(15,True)
    time.sleep(1)
    #turn off LED and wait 1 second 
    GPIO.output(15,False)
    print 'blinking'
    time.sleep(1)
