import socket

ip = "192.168.1.11" # IP of Raspberry Pi

# start server
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((ip, 8080))
serv.listen(5)
print("SERVER: started")

while True:
    # establish connection
    conn, addr = serv.accept()
    from_client = ''
    print("SERVER: connection to Client established")

    while True:
        # receive data and print
        data = conn.recv(4096).decode()
        if not data: break
        print(data)
        from_client += data
        print("Recieved: " + from_client)

        # send message back to client
        msg = "Opening Latch"
        conn.send(msg.encode())

    # close connection and exit
    conn.close()
    break