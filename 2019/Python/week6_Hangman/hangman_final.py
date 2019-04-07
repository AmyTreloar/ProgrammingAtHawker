import time
from random import choice


def get_words_from_file(filename):
    with open(filename) as fp:
        words = fp.readlines()
    return words


def choose_random_word(list_of_words):
    return choice(list_of_words).strip()


def get_hidden_word(word):
    out = []
    for i in range(len(word)):
        out.append('_')
    return out


def process_guess(chosen, hidden, guess, current_fails):
    if chosen.count(guess) <= 0:
        return hidden, current_fails + 1
    for i in range(len(chosen)):
        if chosen[i] == guess:
            hidden[i] = guess
    return hidden, current_fails


def test_end_conditions(curr_fail, max_fail, chosen, hidden):
    if curr_fail >= max_fail:
        return False
    if ''.join(hidden) == chosen:
        return False
    return True


def get_frequency_analysis(file_name, list_of_words, guesses, hidden_word):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
    letters_count = [0] * len(letters)
    print(letters)
    print(letters_count)
    new_list_of_words = []
    for word in list_of_words:
        word = word.strip()
        if len(word) != len(hidden_word):
            continue
        if guess not in word:
            continue
        new_list_of_words.append(word)
        for letter in word:
            if letter in letters:
                i = letters.index(letter)
                letters_count[i] += 1
            else:
                letters.append(letter)
                letters_count.append(1)
    return letters, letters_count, new_list_of_words


def next_letter(letters, letters_count):
    max_number = max(letters_count)
    i = letters_count.index(max_number)
    letter = letters[i]
    letters_count[i] = 0
    return letter


file_name = 'good_words.txt'
list_of_words = get_words_from_file(file_name)
chosen_word = choose_random_word(list_of_words)
hidden_word = get_hidden_word(chosen_word)
guesses = []
playing = True
max_fails = 10
current_fails = 0
print(chosen_word)

while playing:
    letters, letters_count, list_of_words = get_frequency_analysis(file_name, list_of_words, guesses, hidden_word)
    print(f'Current guess {"".join(hidden_word)}. You have {max_fails - current_fails} chances left.')
    guess = next_letter(letters, letters_count)
    print(f"You guessed {guess}")
    hidden_word, current_fails = process_guess(chosen_word, hidden_word, guess, current_fails)
    playing = test_end_conditions(current_fails, max_fails, chosen_word, hidden_word)
    time.sleep(1)

if ''.join(hidden_word) == chosen_word:
    print("You are the winner!")
else:
    print(f"You are a loser! The word was {chosen_word}")
