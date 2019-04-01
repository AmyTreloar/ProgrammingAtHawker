import time
from random import choice


def get_word_from_file(filename):
    with open(filename) as fp:
        words = fp.readlines()
    return choice(words).strip()


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

file_name = 'good_words.txt'
chosen_word = get_word_from_file(file_name)
hidden_word = get_hidden_word(chosen_word)
playing = True
max_fails = 10
current_fails = 0
print(chosen_word)


while playing:
    print(f'Current guess {"".join(hidden_word)}. You have {max_fails - current_fails} chances left.')
    guess = input("Guess a letter: ")
    print(f"You guessed {guess}")
    hidden_word, current_fails = process_guess(chosen_word, hidden_word, guess, current_fails)
    playing= test_end_conditions(current_fails, max_fails, chosen_word, hidden_word)
    time.sleep(1)

if ''.join(hidden_word) == chosen_word:
    print("You are the winner!")
else:
    print(f"You are a loser! The word was {chosen_word}")
