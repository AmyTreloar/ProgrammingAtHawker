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





# key = 13
# message = "Three people can keep a secret, if two of them are dead!"
# cipher = ceaser_cipher(message, key)
# print(cipher)
# plaintext = ceaser_cipher(cipher, key, DECRYPT)
# print(plaintext)
