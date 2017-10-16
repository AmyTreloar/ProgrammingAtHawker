import os

os.rename("account_details", "account_details")

try:

    file = open("account_details", "r")
except OSError:
    print("file not found")
else:
    for line in file:
        print(line)

