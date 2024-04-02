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

def adc():
    v_t = [0 for i in range(8)]
    for v in range(8):
        s = 0
        for i in range(len(v_t)):
            s += 2**(7-i) * v_t[i]
        #print(s)
        time.sleep(0.0005)
        sig = perevod(2**(7-v) + s)
        GPIO.output(dac, sig)
        time.sleep(0.0005)
        compv = GPIO.input(comp)
        if compv == 1:
            v_t[v] = 0
        else:
            v_t[v] = 1
    s=0
    for i in range(len(v_t)):
            s += 2**(7-i) * v_t[i]
    return s
try:
    while True:
        v = adc()
        vol = v / 256 * 3.3
        sig = perevod(v)
        time.sleep(0.0005)
        compv = GPIO.input(comp)
        print(f'adc = {v}, volts {round(vol, 3)}')
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

  
