import socket
# from raspi.latch import Latch
import RPi.GPIO as GPIO
import time

latchPin = 3
proxPin = 11
buzzerPin = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(latchPin, GPIO.OUT)
GPIO.setup(buzzerPin, GPIO.OUT)
GPIO.setup(proxPin, GPIO.IN)
ip = "192.168.1.7" # IP of Raspberry Pi

# start server
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((ip, 8080))
serv.listen(5)
print("SERVER: started")

while True:
    val = GPIO.input(proxPin)
    if val == 0:
        GPIO.output(buzzerPin,GPIO.HIGH)
        time.sleep(2)
        break
    
GPIO.output(buzzerPin,GPIO.LOW)

GPIO.output(latchPin, GPIO.LOW)

while True:
    # establish connection
    conn, addr = serv.accept()
    from_client = ''
    print("SERVER: connection to Client established")
    # latch = Latch()
    
    while True:
        # receive data and print
        print("Start")
        data = conn.recv(4096).decode()
        if not data: break
        print(data)
        from_client += data
        print("Recieved: " + from_client)

        if data == 'Access Granted':
            # latch.latch_open()
            GPIO.output(latchPin, GPIO.HIGH)
            time.sleep(5)
            GPIO.output(latchPin, GPIO.LOW)
            # send message back to client
            msg = "Opening Latch"
            conn.send(msg.encode())
            break

    # close connection and exit
    conn.close()
    break