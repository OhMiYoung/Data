import RPi.GPIO as GPIO
import time

LED = 26

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

GPIO.output(LED, GPIO.HIGH)

time.sleep(3)
GPIO.output(LED, GPIO.LOW)

for i in range(5):
    GPIO.setup(LED, GPIO.OUT)

    GPIO.output(LED, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(1)