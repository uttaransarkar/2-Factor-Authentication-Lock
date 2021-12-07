import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN)
GPIO.setup(5, GPIO.OUT)

while True:
    val = GPIO.input(3)
    if val == 0:
        GPIO.output(5,GPIO.HIGH)
    else:
        GPIO.output(5,GPIO.LOW)