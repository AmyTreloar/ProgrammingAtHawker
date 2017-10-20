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
    msg = msg.decode("utf-8")
    id, msg_type, msg = msg.split(':')
    client.send("SVR:ECHO:{} {}!\r\n".format(id, msg).encode('ascii'))
    client.close()



