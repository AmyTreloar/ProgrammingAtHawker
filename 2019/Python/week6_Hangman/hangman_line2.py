import random


def get_word_from_file(file_name):
    '''
    Returns a random word from a file of words. 
    Return: random word. 
    '''
    with open(file_name, 'r') as fp:
        hangman_words = fp.readlines()
    output_word = random.choice(hangman_words).rstrip()
    return output_word


def make_hidden_word(word):
    '''
    Creates a hidden word of the same length as the word
    given. 
    For example, if the word is "Adam", returns "____"
    Return: a string
    '''
    output_word = ''
    # output_word = '_'*len(word)
    for letter in word:
        output_word += '_'
    return output_word


def make_guess(hidden_word):
    """
    Make guess allows the user to select a letter and
    and if the letter is available, reveals the letter in
    the word
    :param hidden_word: a hidden list of letters. i.e., 'adam' would be seen as "____"
    :return: a list of hidden letters
    """
    guess = input("Guess a letter: ")
    for i in range(0, len(random_word)):
        if random_word[i] == guess:
            hidden_word[i] = guess
    return hidden_word


random_word = get_word_from_file('good_words.txt')
hidden_word = list(make_hidden_word(random_word))
while True:
    print(random_word, ''.join(hidden_word))
    make_guess(hidden_word)
