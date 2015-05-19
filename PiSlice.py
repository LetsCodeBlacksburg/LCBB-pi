import RPi.GPIO as GPIO
import time
import os
import glob
import thread

DATAIN = 13
CLOCK = 11
LOCK = 12

chars = [
0b00000011, #0
0b10011111, #1
0b00100101, #2
0b00001101, #3
0b10011001, #4
0b01001001, #5
0b01000001, #6
0b00011111, #7
0b00000001, #8
0b00001001  #9
]

def shift(input):

 if input == 1:
  input=True
 else:
  input=False

 GPIO.output(DATAIN,input)
 GPIO.output(CLOCK,GPIO.HIGH)
 GPIO.output(CLOCK,GPIO.LOW)
 GPIO.output(DATAIN,GPIO.LOW)

def shift_byte(number):
 for x in range(0,8):
  shift((number>>x)%2)

number = 0
def display_number(tName):
 while True:
  st = '%0*d' % (8, number)
  for x in range(0, 8):
   GPIO.output(LOCK,GPIO.LOW)
   shift_byte(1 << 7 >> x)
   shift_byte(chars[int(st[x])])
   GPIO.output(LOCK,GPIO.HIGH)

def init():
 GPIO.setmode(GPIO.BOARD)
 GPIO.setwarnings(False)
 GPIO.setup(DATAIN, GPIO.OUT)
 GPIO.setup(CLOCK, GPIO.OUT)
 GPIO.setup(LOCK, GPIO.OUT)
 thread.start_new_thread(display_number, ("DispThread", ))

def init_temp():
 os.system('modprobe w1-gpio')
 os.system('modprobe w1-therm')

 base_dir = '/sys/bus/w1/devices/'
 device_folder = glob.glob(base_dir + '28*')[0]
 device_file = device_folder + '/w1_slave'



def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return int(temp_c), int(temp_f)