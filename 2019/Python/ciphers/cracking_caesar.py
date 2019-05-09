import operator
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789?!., '
cipher = "nzzvy@55vxumxgssotm:94}o~yozk4ius5vxumxgssotm"
#cipher = 'P1Z2 76R4 M5PV R0PR MV5M 01MZ 14RM NO17 6MP1 Z276 R45M 6UN0 MN56 4101 Z!MV 5MNO 176M 6RYR 5P12 R5MM RQ5T R4M9 KMQV WX56 4N'
cipher = ''.join(cipher.split(" "))


def get_letter_frequencies_list(doc):
    letters = {}
    for line in doc:
        words = line.split(" ")
        for word in words:
            word = word.upper().strip()
            for letter in word:
                if letter in letters:
                    letters[letter] += 1
                else:
                    letters[letter] = 1
    return letters

def get_letter_frequencies(file_name):
    with open(file_name) as fp:
        doc = fp.readlines()
    return get_letter_frequencies_list(doc)


def decrypt_caeser_cipher(msg, key):
    out = ''
    for symbol in msg:
        symbol = symbol.upper()
        if symbol not in SYMBOLS or symbol == '':
            continue
        symbol_index = SYMBOLS.find(symbol)
        translated_index = symbol_index - key
        if translated_index < 0:
            translated_index += len(SYMBOLS)
        out += SYMBOLS[translated_index]
    return out

def check_possible_crack(msg):
    words_in_msg = 0
    with open('sample_text.txt') as fp:
        doc = fp.readlines()
    for line in doc:
        words = line.split(" ")
        for word in words:
            word = word.upper().strip()
            if len(word) <= 3:
                continue
            if word in msg:
                words_in_msg += 1
    return words_in_msg

def shift_crack(cipher):
    messages = []
    key = 0
    for i in range(0, len(SYMBOLS)):
        potential = decrypt_caeser_cipher(cipher, i)
        print(f'Shift={i} | {potential}')
        potential_count = check_possible_crack((potential))
        if potential_count > 1:
            messages.append((i, potential))
    return messages

def get_ordered_list_of_letters(word_freqs):
    letters = list(word_freqs.keys())
    letters_count = list(word_freqs.values())
    letters_ordered_by_frequency = []
    looping = True
    while looping:
        max_count = max(letters_count)
        count_index = letters_count.index(max_count)
        letters_ordered_by_frequency.append(letters[count_index])
        letters_count[count_index] = -1
        looping = False
        for count in letters_count:
            if count >= 0:
                looping = True
    return letters_ordered_by_frequency
import time
def freq_crack(cipher, word_freqs):
    message = ''
    cipher = list(cipher)
    message = ['_']*len(cipher)
    cipher_symbols_frequency = get_letter_frequencies_list(word_freqs)
    cipher_symbols_ordered = get_ordered_list_of_letters(cipher_symbols_frequency)


    letters_ordered = get_ordered_list_of_letters(word_freqs)

    for i in range(0, len(cipher_symbols_ordered)):
        for j in range(0, len(cipher)):
            if cipher[j] == cipher_symbols_ordered[i]:
                message[j] = letters_ordered[i]
        #     print(message[j], end='')
        # print()
        # time.sleep(0.25)
    print("C", cipher_symbols_ordered)
    print("L", letters_ordered)

    return ''.join(message)

print('Cipher to crack', cipher)
#print('shift_crack: ', 'most likely plaintext ', shift_crack(cipher))
print('freq_crack: ', ' most likely plaintext ' ,freq_crack(cipher, get_letter_frequencies('sample_text.txt')))
print('Cipher to crack', cipher)
#print("Actual plain text", "Cryptanalysis of the Enigma ciphering system enabled the western Allies in World War II to read substantial amounts of Morse-coded radio communications of the Axis powers that had been enciphered using Enigma machines. This yielded military intelligence which, along with that from other decrypted Axis radio and teleprinter transmissions, was given the codename Ultra. This was considered by western Supreme Allied Commander Dwight D. Eisenhower to have been 'decisive' to the Allied victory.".upper())