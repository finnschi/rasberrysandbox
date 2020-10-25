##Doorbell Buttler V0.1
##Finn Jager
##sends a push message using apprise when Doorbell is pushed
##Dorbell connected to a Realais that switches on/off when doorbell is pushed.
import RPi.GPIO as GPIO
##needs python3 for me
import apprise
## pip3 install apprise
apobj = apprise.Apprise()
config = apprise.AppriseConfig()
config.add('/home/pi/.config/apprise')
##config file needs to have the URL/pravatekey e.tc
apobj.add(config)
def button_callback(channel):
    apobj.notify(
        body='YOUR DOORBELL IS BELLING GO RUN NOW!',
        title='DoorBellBot_v0.1',
    )
    print("push detected!")
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
##no power on the GPIO pin, so its 0 by default, once it switches it will get 3V thus we can detect the change
GPIO.add_event_detect(8,GPIO.BOTH,callback=button_callback)
##exit for debugging
message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up