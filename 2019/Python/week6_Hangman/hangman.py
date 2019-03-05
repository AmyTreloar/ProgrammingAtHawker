import random

words = []
with open('good_words.txt') as fp:
    words = fp.readlines()

word_number = random.randint(0, len(words))
answer = words[word_number].strip()
secret = []
for i in range(0, len(answer)): 
    secret.append('_')
print(answer, secret)

guesses_left = 8
while True:
    guess = input("Guess a letter: ")
    guess_count = answer.count(guess)
    print(answer.find(guess), guess_count)

    for i in range(0, len(answer)):
        if guess == answer[i]:
            secret[i] = guess
    print(secret)
