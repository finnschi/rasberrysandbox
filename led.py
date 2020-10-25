import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(10,GPIO.OUT, initial=GPIO.LOW)
while True: # Run forever
    GPIO.output(10, GPIO.HIGH) # Turn on
    sleep(.1)                  # Sleep for 1 second
    GPIO.output(10, GPIO.LOW)  # Turn off
    sleep(.1)                  # Sleep for 1 second