import random


def get_word_from_file(filename):
    pass


def construct_hidden_word(chosen_word):
    pass


def is_guess_in_word(guess, chosen_word):
    pass


def process_guess(chosen_word, hidden_word, guess):
    pass


def test_end_conditions(max_guess, current_guesses, hidden_word):
    pass


GAME_RUNNING = True
MAX_GUESSES = 5
CURRENT_GUESSES = 0

while GAME_RUNNING:
    chosen_word = get_word_from_file("good_words.txt")
    hidden_word = construct_hidden_word(chosen_word)
    guess = input("Guess a letter: ")
    CURRENT_GUESSES = is_guess_in_word(guess, chosen_word)
    hidden_word = process_guess(chosen_word, hidden_word, guess)
    GAME_RUNNING = test_end_conditions(MAX_GUESSES, CURRENT_GUESSES, hidden_word)
