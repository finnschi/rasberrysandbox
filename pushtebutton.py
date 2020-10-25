import RPi.GPIO as GPIO
import apprise
apobj = apprise.Apprise()
config = apprise.AppriseConfig()
config.add('/home/pi/.config/apprise')
apobj.add(config)
def button_callback(channel):
    apobj.notify(
        body='YOUR DOORBELL IS BELLING GO RUN NOW!',
        title='DoorBell',
    )
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(8,GPIO.RISING,callback=button_callback)

message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up