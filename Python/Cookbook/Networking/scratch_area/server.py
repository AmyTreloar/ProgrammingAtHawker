import socket
import time

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)

while True:
    client, address = s.accept()
    msg = client.recv(1024)
    print(msg)

    msg = msg
    client.send("ACK: Yes you are {}!\r\n".format(id).encode('ascii'))
    client.close()



