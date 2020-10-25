import RPi.GPIO as GPIO
import http.client, urllib
def button_callback(channel):
    print("Dont push me cause I am close to the edge..")
    conn = httplib.HTTPSConnection("pushsafer.com:443")
    conn.request("POST", "/api",
                 urllib.urlencode({
                     "k": "077tGJYCAJfX4NGoqlP4",  # Your Private or Alias Key
                     "m": "BUTTON WAS PRESSED!!!",  # Message Text
                     "t": "DI DUM",  # Title of message
                     "i": "1",  # Icon number 1-98
                     "s": "0",  # Sound number 0-28
                     "v": "3",  # Vibration number 0-3
                 }), {"Content-type": "application/x-www-form-urlencoded"})
    response = conn.getresponse()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(8,GPIO.RISING,callback=button_callback)

message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up