import time

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789?!.,'
ENCRYPT = 0
DECRYPT = 1


def ceaser_cipher(msg, key, mode=ENCRYPT):
    out = ''
    for symbol in msg:
        symbol = symbol.upper()
        if symbol not in SYMBOLS:
            continue

        symbol_index = SYMBOLS.find(symbol)
        if mode == ENCRYPT:
            translated_index = symbol_index + key
        elif mode == DECRYPT:
            translated_index = symbol_index - key

        if translated_index >= len(SYMBOLS):
            translated_index -= len(SYMBOLS)
        elif translated_index < 0:
            translated_index += len(SYMBOLS)
        out += SYMBOLS[translated_index]
    return out


def find_words_in_text(words, msg_in):
    out = 0
    for word in words:
        word = word.upper().strip()
        if len(word) < 3:
            continue
        if word in msg_in:
            out+=1
    return out


cipher = "6U4RR2R12YRPN0XRR2N5RP4R6MVS6911S6URZN4RQRNQK"
plain_text = ''
candidites = []

with open('good_words.txt') as fp:
    words = fp.readlines()

# words = ["three"]

for i in range(0, 26):
    test = ceaser_cipher(cipher, i, DECRYPT)
    print(i, test)
    words_found = find_words_in_text(words, test)
    if words_found >= 5:
        candidites.append(test)

for c in candidites:
    print(c)
print(len(candidites))