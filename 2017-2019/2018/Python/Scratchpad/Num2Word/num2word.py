words = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven']


def main(number):
    word = words[number]
    if word is not None:
        print(words[number])
    else:
        print("Error: value not defined.")



main(1)
main(2)
main(3)
main(4)
main(5)
main(6)
main(7)
