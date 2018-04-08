import os

with open("names.txt") as f:
    for line in f:
        name = line.strip()
        path = f'./{name}/'
        if not os.path.exists(path):
            os.makedirs(path)

