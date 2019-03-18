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
    #output_word = '_'*len(word)
    for letter in word:
        output_word += '_'
    return output_word

random_word = get_word_from_file('good_words.txt')
hidden_word = make_hidden_word(random_word)

print(random_word, hidden_word)