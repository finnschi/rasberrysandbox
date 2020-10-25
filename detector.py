import RPi.GPIO as GPIO
import time
def button_callback(channel):
    print("push detected!")
    GPIO.output(10, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(10, GPIO.LOW)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(8,GPIO.BOTH,callback=button_callback)
message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up