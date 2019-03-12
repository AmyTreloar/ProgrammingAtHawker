def greet(person_name, greeting):
    person_name = person_name.title()
    return f"{greeting}, {person_name}"


def say_hello(person_name):
    return greet(person_name, "Hello")


def say_goodbye(person_name):
    return greet(person_name, "Goodbye")


while True:
    name = input("What is your name? ")
    print(say_hello(name))
