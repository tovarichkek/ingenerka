import RPi.GPIO as GPIO
import time
def binary(val):
    return [int(i) for i in bin(val)[2:].zfill(8)]

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    t = float(input())
except ValueError:
    if type(t) == str:
        print('Значение должно числом')
    else:
        print('Значение меньше 0') 
while True:
    for i in range(256):
        GPIO.output(dac, binary(i))
        time.sleep(t)
    for i in range(255, -1,-1):
        GPIO.output(dac, binary(i))
        time.sleep(t)
GPIO.output(dac, 0)
GPIO.cleanup()