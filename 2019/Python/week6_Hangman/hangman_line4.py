import random

with open('good_words.txt') as fp:
    words = fp.readlines()

random_word = random.choice(words).strip()
hidden_word = ''
for letter in random_word:
    hidden_word += '_'
print(random_word, hidden_word)