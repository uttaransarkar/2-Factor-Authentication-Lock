import socket
from start import *

ip = "192.168.1.7" # IP of Raspberry Pi

# connect to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, 8080))
print("CLIENT: connected")

access=start()
print(access)
# send a message
msg='Access Denied'
if access:
    msg='Access Granted'
client.send(msg.encode())

# recive a message and print it
from_server = client.recv(4096).decode()
print("Recieved: " + from_server)

# exit
client.close()