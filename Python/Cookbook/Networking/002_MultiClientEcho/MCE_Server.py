from threading import Thread
import socket
import sys

clients = []

server = socket.socket()
host = socket.gethostname()
port = 12345

server.bind((host, port))

server.listen(10)
print("Server {} listening on port {}".format(host, port))


def handle_client(client, address, name):
    while True:
        msg = client.recv(1024).decode('utf-8')
        print("{} MSG -> {}".format(name, msg))
        for c in clients:
            if c['name'] != name:
                c['client'].send("{}: {}".format(name, msg).encode('ascii'))


def make_client(client, address, name):
    return {
        'client': client,
        'address': address,
        'name': name
    }


while True:
    client, address = server.accept()
    print("Client connected: {}".format(address), file=sys.stderr)
    initial_cmd = client.recv(1024).decode('utf-8')
    cmd, arg = initial_cmd.split(":")
    if cmd == "CLIENT_NAME":
        name = arg
    else:
        continue
    c = make_client(client, address, name)
    clients.append(c)
    Thread(target=lambda: handle_client(client, address, name)).start()
