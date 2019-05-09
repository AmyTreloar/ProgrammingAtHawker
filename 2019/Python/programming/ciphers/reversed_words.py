def reverse_words_in_message(msg_in):
    words = msg_in.split(" ")
    out = []
    for word in words:
        out.append(''.join(reversed(word)).upper())
    return ' '.join(out)


message = "Three people can keep a secret, if two of them are dead"
cipher = reverse_words_in_message(message)
print(cipher)
plaintext = reverse_words_in_message(cipher)
print(plaintext)