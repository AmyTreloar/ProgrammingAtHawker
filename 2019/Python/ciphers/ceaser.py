#SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789?!.,' "
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ENCRYPT = 0
DECRYPT = 1


def caesar_cipher_lean(msg, key, mode=ENCRYPT):
    out = ''
    translated_index = 0
    if mode == DECRYPT:
        key = 0 - key
    for symbol in msg:
        symbol = symbol.upper()
        if symbol not in SYMBOLS or symbol == '':
            continue
        symbol_index = SYMBOLS.find(symbol)
        translated_index = symbol_index + key
        if translated_index >= len(SYMBOLS):
            translated_index -= len(SYMBOLS)
        elif translated_index < 0:
            translated_index += len(SYMBOLS)
        out += SYMBOLS[translated_index]
    return out


def ceaser_cipher(msg, key, mode=ENCRYPT):
    out = ''
    translated_index = 0
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


key = 1
message = "Cryptanalysis of the Enigma ciphering system enabled the western Allies in World War II to read substantial amounts of Morse-coded radio communications of the Axis powers that had been enciphered using Enigma machines. This yielded military intelligence which, along with that from other decrypted Axis radio and teleprinter transmissions, was given the codename Ultra. This was considered by western Supreme Allied Commander Dwight D. Eisenhower to have been 'decisive' to the Allied victory."
#message = "COMPUTER SCIENCE IS NO MORE ABOUT COMPUTERS THAN ASTRONOMY IS ABOUT TELESCOPES  EDSGER W. DIJKSTRA"
cipher = ceaser_cipher(message, key)
cipher2 = caesar_cipher_lean(message, key)
print(message)
print(cipher)
print(cipher2)
# # print(cipher)
# plaintext = ceaser_cipher(cipher, 3, DECRYPT)
# plaintext2 = caesar_cipher_lean(cipher2, key, DECRYPT)
# print(plaintext)
# print(plaintext2)
# out = [cipher[i:i + 4] for i in range(0, len(plaintext), 4)]
# print(' '.join(out))
#todo: implement each of the tree ciphers as per google classroom
#todo: Brute force cracker for ceaser cipher
#todo: apply a frequency analysis for the ceaser cipher