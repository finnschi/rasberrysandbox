import RPi.GPIO as GPIO
#import http.client, urllib
from pushsafer import init, Client
init("077tGJYCAJfX4NGoqlP4")
def button_callback(channel):
    print("Dont push me cause I am close to the edge..")
    Client("").send_message("Message", "Hello", "323", "1", "4", "2", "https://www.pushsafer.com", "Open Pushsafer", "0", "2", "60", "600", "1", "", "", "")

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(8,GPIO.RISING,callback=button_callback)

message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up