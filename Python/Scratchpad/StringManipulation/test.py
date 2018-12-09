def make_stats_dict():
    letters = {}
    a = 65
    z = 90
    i = a
    while i <= z:
        letters[chr(i)] = 0
        i += 1
    return letters


def letter_stats(letters):
    with open('words', 'r') as words:
        for word in words:
            word = word.strip('\r\n')
            for letter in word:
                letter = letter.upper()
                letters[letter] += 1
    return letters


def findWord(w):
    with open('words', 'r') as words:
        for line in words:
            line = line.strip("\r\n")
            if w == line:
                return True
        return False


message = "Three can keep a secret if two of them are dead"


def reverse(msg):
    msg = msg.upper()
    msg = msg.split(" ")
    out = []
    for word in msg:
        i = len(word) - 1
        tmp_out = ''
        while i >= 0:
            tmp_out += word[i]
            i -= 1
        out.append(tmp_out)

    return ' '.join(out)


def ceaser(msg, key, encrypting=True):
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.!/|\\'
    msg = msg.upper()
    translated = ''
    translated_index = None
    for symbol in msg:
        if symbol not in SYMBOLS:
            translated += symbol
            continue
        symbol_index = SYMBOLS.find(symbol)
        if encrypting:
            translated_index = symbol_index + key
        else:
            translation_index = symbol_index - key

        if translated_index > len(SYMBOLS):
            translated_index = translated_index - len(SYMBOLS)
        elif translated_index < 0:
            translated_index = translated_index + len(SYMBOLS)
        translated += SYMBOLS[translated_index]
    return translated


letters = make_stats_dict()
print(letters)
letters = letter_stats(letters)
print(letters)
reverse_cipher = reverse(message)
ceaser_cipher = ceaser(message, 13)
print(f'{message}\r\n{reverse_cipher}')
print()
print(f'{message}\r\n{ceaser_cipher}')
