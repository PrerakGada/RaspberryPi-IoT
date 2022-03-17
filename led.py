import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(18,GPIO.OUT)

for x in range(15):
    time.sleep(0.1)

    GPIO.output(18,GPIO.HIGH)

    time.sleep(0.1)

    GPIO.output(18,GPIO.LOW)
