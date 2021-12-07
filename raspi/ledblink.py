import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)

count = 0
while count<5:
    GPIO.output(3, True)
    time.sleep(1)
    GPIO.output(3, False)
    time.sleep(1)
    count+=1