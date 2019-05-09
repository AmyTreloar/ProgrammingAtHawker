import random

file_name = 'good_words.txt'
with open(file_name) as fp:
    words = fp.readlines()

random_word = random.choice(words)
print(random_word)
