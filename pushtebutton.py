import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
        input_value = GPIO.input(8)
        print(input_value)
        if input_value == GPIO.HIGH:
            print("Dont push me cause I am close to the edge..")