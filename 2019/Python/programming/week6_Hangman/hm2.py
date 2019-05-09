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




def test_end_conditions(curr_fail, max_fail, chosen, hidden):
    if curr_fail > max_fail:
        return False
    if ''.join(hidden) == chosen:
        return False
    return True


file_name = 'better_words.txt'
chosen_word = get_word_from_file(file_name)
hidden_word = get_hidden_word(chosen_word)

playing = True
max_fails = 10
current_fails = 0
print(chosen_word)


while playing:
    print(f'Current guess {"".join(hidden_word)}. You have {max_fails - current_fails} chances left.')
    guess = input("Guess a letter: ")
    uess = get_guess(letters, letters_count)
    print(f"You guessed {guess}")
    #todo update the stats based off of what we know
    playing = test_end_conditions(current_fails, max_fails, chosen_word, hidden_word)
    time.sleep(1)

if ''.join(hidden_word) == chosen_word:
    print("You are the winner!")
else:
    print(f"You are a loser! The word was {chosen_word}")
