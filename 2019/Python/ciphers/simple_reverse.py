def simple_reverse_cipher(msg_in):
    out = ''
    for i in reversed(range(len(msg_in))):
        out += msg_in[i].upper()
    return out


message = "Three people can keep a secret, if two of them are dead"
cipher = simple_reverse_cipher(message)

print(cipher)

plaintext = simple_reverse_cipher(cipher)

print(plaintext)
