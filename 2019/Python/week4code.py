def greet_users(names, known_names):
    for name in names:
        if name in known_names:
            print(f"Hey, {name.title()}, how are you going?")
        else:
            print(f"Good to meet you {name.title()}")

    
known_names = ["adam", 'betty', 'eddie']
s_names = ['adam', 'bob', 'charlie']
greet_users(s_names, known_names)