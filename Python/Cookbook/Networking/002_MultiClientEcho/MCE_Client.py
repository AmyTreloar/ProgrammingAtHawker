from threading import Thread
from random import choice
from random import randint
from time import sleep
import socket
import string

msgs = [
    "Wubbalubbadubdub!",
    "And that's the wayyyyyy the news goes!",
    "Uh ohhhh! Somersault jump!",
    "And that's why I always say, 'Shumshumschilpiddydah!'",
    "No jumping in the sewer.",
    "BURGERTIME!",
    "Rubber baby buggy bumpers!",
    "GRASSSSS... tastes bad!",
    "i love my grandkids!",
    "Calm down Morty, you gotta listen to me, Morty"
]


def rick_roll(client_socket):
    while True:
        msg = choice(msgs)
        client_socket.send(msg.encode('ascii'))
        sleep(5)


def inbound_msgs(client_socket):
    while True:
        msg = client_socket.recv(1024).decode('utf-8')
        print(msg)


def main():
    ricks = 2
    for i in range(0, ricks):
        name = "{}-{}".format(choice(string.ascii_lowercase), randint(1, 999))
        print(name)
        client_socket = socket.socket()
        host = socket.gethostname()
        port = 12345
        client_socket.connect((host, port))
        client_socket.send("CLIENT_NAME:{}".format(name).encode('ascii'))
        Thread(target=lambda: rick_roll(client_socket)).start()
        Thread(target=lambda: inbound_msgs(client_socket)).start()
        sleep(randint(1, 5))


if __name__ == "__main__":
    main()
