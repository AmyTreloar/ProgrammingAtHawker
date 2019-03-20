import random


def get_word(file_name):
    with open(file_name) as fp:
        words = fp.readlines()
    return random.choice(words).strip()


def get_hidden_word(word):
    out = ''
    for letter in word:
        out += '_'
    return list(out)


random_word = get_word("good_words.txt")
hidden_word = get_hidden_word(random_word)
#all letters found!
#running out of guesses!

guesses=0
max_guesses = 3
while guesses <= max_guesses:
    print(random_word, ''.join(hidden_word), f'Guesses left {max_guesses - guesses}')
    guess = input("Guess a letter: ")
    found_letter = False
    for i in range(0, len(random_word)):
        if guess == random_word[i]:
            found_letter = True
            hidden_word[i] = guess

    if not found_letter:
        guesses += 1



