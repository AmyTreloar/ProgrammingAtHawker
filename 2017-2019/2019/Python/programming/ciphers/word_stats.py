import os

alpha = 'abcdefghijklmnopqrstuvwxyz'

class child_node():
    def __init__(self, letter, count=0):
        self.letter = letter
        self.count = count

    def __str__(self):
        return f"{self.letter}, {self.count}"

class LetterTree():
    def __init__(self, letter=None):
        self.letter = letter
        self.children = []


    def add_child(self, child_letter):
        found = False
        for child in self.children:
            if child.letter == child_letter:
                child.count += 1
                found = True
        if not found:
            self.children.append(child_node(child_letter))

    
    def __str__(self):
        if self.letter == None:
            out = []
            for child in self.children:
                out += f"[{child.letter}{child.count}]"
            out = ''.join(out)
            return f"Start Node, {out}"
        return f"{self.letter}, {out}"


# file = "./python/programming/ciphers/better_words.txt"
# with open(file) as fp:
#     words = fp.readlines()

# words = [x.strip() for x in words]

words = [
    'adam',
    'john',
    'jon', 
    'debbi'
]

start = LetterTree()

for symbol in alpha: 
    start.add_child(symbol)

for word in words:
    node = start
    for letter in word:
        node.add_child(letter)



print(start)