import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(16,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(18,GPIO.OUT, initial=GPIO.LOW)
while True: # Run forever
    GPIO.output(18, GPIO.LOW)
    GPIO.output(12, GPIO.HIGH)
    sleep(5)
    GPIO.output(16, GPIO.HIGH)
    sleep(1)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(18, GPIO.HIGH)
    sleep(5)