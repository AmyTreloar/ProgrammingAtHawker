from random import choice
import socket

client_socket = socket.socket()
host = socket.gethostname()
port = 12345

name = "test_client"

msgs = [
    "Wubbalubbadubdub!",
    "And that's the wayyyyyy the news goes!",
    "Uh ohhhh! Somersoult jump!",
    "And that's why I always say, 'Shumshumschilpiddydah!'",
    "No jumping in the sewer.",
    "BURGERTIME!",
    "Rubber baby buggy bumpers!",
    "GRASSSSS... tastes bad!",
    "i love my grandkids!",
    "Calm down Morty, you gotta listen to me, Morty"
]
msg_out = choice(msgs)
client_socket.connect((host, port))
client_socket.send(msg_out.encode('ascii'))
msg_recv = client_socket.recv(1024).decode('utf-8')
print(msg_recv)
