import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT, initial = 0)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)

def perevod(value):
    res = bin(value)
    res1 = res[2:]
    res11 = res1.zfill(8)
    res2 = [int(x) for x in res11]
    return res2

def adc(v):
    sig = perevod(v)
    GPIO.output(dac, sig)
    return sig

try:
    while True:
        for v in range(256):
            sig = adc(v)
            time.sleep(0.0005)
            vol = v / 256 * 3.3
            compv = GPIO.input(comp)
            if compv == 1:
                print(f'adc = {v}, volts {round(vol, 3)}')
                #time.sleep(2)
                break
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

  


