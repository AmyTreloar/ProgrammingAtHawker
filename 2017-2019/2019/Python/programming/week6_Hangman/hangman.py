import random


def init_game():
    """
    Initialises the game state.
    Reads through a file, chooses a name by random, and returns both the
    random name and hidden name for students as a list
    :return: rnd_word (string), rnd_secret (a list of characters)
    """
    with open('good_words.txt') as fp:
        words = fp.readlines()
    rnd_word = random.choice(words).strip()
    rnd_secret = []
    for i in range(len(rnd_word)):
        rnd_secret.append('_')
    return rnd_word, rnd_secret


def test_end_conditions(secret, current_fails, max_fails):
    """

    :param secret:
    :param current_fails:
    :param max_fails:
    :return:
    """
    if '_' not in secret:
        print("You are the winner!")
        return False
    if current_fails >= max_fails:
        print("You lose, the man is hung!")
        return False
    return True


def get_guess(answer, secret, max_fails, current_fails):
    print(f"You have {max_fails - current_fails} guesses left.")
    guess = input(f"{''.join(secret)} Guess a letter: ")
    guess_count = answer.count(guess)
    return guess, guess_count


def process_guess(guess, guess_count, answer, secret):
    if guess_count <= 0:
        return 1

    for i in range(len(answer)):
        if guess == answer[i]:
            secret[i] = guess
    return 0


def main_loop():
    answer, secret = init_game()
    playing = True
    max_fails = 8
    current_fails = 0
    print(answer)
    while playing:
        guess, guess_count = get_guess(answer, secret, max_fails, current_fails)
        current_fails += process_guess(guess, guess_count, answer, secret)
        playing = test_end_conditions(secret, current_fails, max_fails)


main_loop()
