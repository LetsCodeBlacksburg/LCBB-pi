import PiSlice

PiSlice.init()
PiSlice.init_temp()

while True:
  c,f = PiSlice.read_temp()
  PiSlice.number = f
  
