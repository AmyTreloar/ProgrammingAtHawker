def authenticate_user(usr='bob', psw="p@55w0rd!"):
    try:
        fp = open("account_details", 'r')
    except OSError:
        print("it can not open")
    else:
        for line in fp:
            line = line.strip('\r\n')
            line = line.split(' ')
            username = line[0]
            password = line[1]
            print("'{}' '{}'".format(username, password))
            if usr == username and psw == password:
                print("WE HAVE AUTHENTICATION")
            else:
                print("Username or password is incorrect or unknown")


authenticate_user()
