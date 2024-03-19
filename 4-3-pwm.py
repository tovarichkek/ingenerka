import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)
p = GPIO.PWM(21, 1000)
duty_cycle = 0
p.start(0)
try:
    while True:
        
        duty_cycle = int(input('заполненность: '))
        p.ChangeDutyCycle(duty_cycle)
        print(duty_cycle*3.3/100)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
