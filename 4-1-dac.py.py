import RPi.GPIO as GPIO

def binary(val):
    return [int(i) for i in bin(val)[2:].zfill(8)]

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
while True:
    try:
        print("Введите число")
        r = input()
        if r == 'q':
            print('Програма завершена')
            break
        test = float(r)*3.3/256
        print(test)

    except TypeError:
        print('Значение должно числом')
    except RuntimeError:
        print('Значение превышает возможный предел')
    except ZeroDivisionError:
        print('Значение меньше 0')
    except ValueError:
        print('Значение должно быть целое')
    GPIO.output(dac, binary(int(r)))

        

    

GPIO.output(dac, 0)
GPIO.cleanup()

