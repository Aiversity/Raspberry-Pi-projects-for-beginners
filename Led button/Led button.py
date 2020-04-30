import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(5, GPIO.IN)
while True:
    
    reading = GPIO.input(5)
    GPIO.output(7, reading)
    print(reading)


