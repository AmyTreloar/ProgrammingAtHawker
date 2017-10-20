import socket
import sys

server = socket.socket()
host = socket.gethostname()
port = 12345

server.bind((host, port))

server.listen(5)
print("Server {} listening on port {}".format(host, port))
while True:
    client, address = server.accept()
    print("Client connected: {}".format(address), file=sys.stderr)
    msg = client.recv(1024).decode('utf-8')
    print("{} MSG -> {}".format(address, msg))
    client.send("ECHO: {}\r\n".format(msg).encode('ascii'))
    client.close()

