usernames = ['admin', 'bob', 'god']
requested_usernames = ['terry', 'paul', 'god']

for requested_username in requested_usernames:
    if requested_username in usernames:
        print(f"Sorry, that username {requested_username} is already taken!")
    else:
        print(f'Congratulations, {requested_username} is free for use!')

