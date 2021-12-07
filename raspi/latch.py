import RPi.GPIO as GPIO
import time

class Latch:
    latchPin = 3
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(latchPin, GPIO.OUT)

    def latch_open(self):
        GPIO.output(self.latchPin, GPIO.HIGH)
        time.sleep(5)
    
    