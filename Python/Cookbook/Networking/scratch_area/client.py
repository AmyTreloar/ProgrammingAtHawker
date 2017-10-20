import socket

import sys

s = socket.socket()
host = socket.gethostname()
port = 12345

name = input("What is your name? ")
s.connect((host, port))
while True:
    out_msg = input("> ")
    if out_msg.lower() == "quit":
        break
    s.send("{}:MSG:{}".format(name, out_msg).encode('ascii'))
    in_msg = s.recv(1024).decode('utf-8')
    #print(in_msg, file=sys.stderr)
    id, msg_type, msg = in_msg.split(':')
    print("{}:{}:{}".format(id, msg_type, msg))
s.close()