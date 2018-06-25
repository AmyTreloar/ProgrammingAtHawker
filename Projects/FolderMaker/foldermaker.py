from shutil import copy2
import os, errno

names = []

with open("names.txt") as names_file:
    print('what', names_file)
    for name in names_file:
        print(name)
        names.append(name.strip("\r\n"))

def make_names_folders(name):
    try:
        os.makedirs(name)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

for name in names:
    make_names_folders(name)
    copy2('Microcontrollers_T_.rtf', f'{name}/Microcontrollers_T_{name}_Assignment1')