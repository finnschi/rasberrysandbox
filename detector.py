import RPi.GPIO as GPIO
def button_callback(channel):
    print("push detected!")

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(8,GPIO.BOTH,callback=button_callback)
message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up