import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN)
while True:
        input_value = GPIO.input(8)
        if input_value == False:
            print("Dont push me cause I am close to the edge..")
            while input_value == False:
                input_value = GPIO.input(8)