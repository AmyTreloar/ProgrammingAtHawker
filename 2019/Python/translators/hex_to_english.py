import binascii


def english_to_hex(msg_in):
    msg_in = msg_in.encode()
    out = binascii.hexlify(bytes(msg_in))
    #mystring.encode('utf-8')
    return str(out,'ascii')

def hex_to_english(msg_in):
    x_unhexed = binascii.unhexlify(msg_in)
    x_ascii = str(x_unhexed, 'ascii')
    return x_ascii

def codeaify(msg_in):
    out = ''
    for i in range(len(msg_in)):
        if i % 2 == 0:
            out += " "
        out += msg_in[i]
    return out

def hex_to_english_letters(msg_in):
    msg = msg_in.split(" ")
    out = ''
    for i in msg:
        msg_unhexed = binascii.unhexlify(i)
        out += str(msg_unhexed, 'ascii')
    return out
msg = 'A stairway to heaven may be an overstatement but the pathway for your quick response starts near numeracy and rises through literacy'
print(msg)
msg = english_to_hex(msg)
msg2 = codeaify(msg)
print(f'hacky code: {msg2}')
print(f'hex: {msg}')
msg = hex_to_english(msg)
print(f'ascii: {msg}')
msg_3 = "41 20 73 74 61 69 72 77 61 79 20 74 6f 20 68 65 61 76 65 6e 20 6d 61 79 20 62 65 20 61 6e 20 6f 76 65 72 73 74 61 74 65 6d 65 6e 74 20 62 75 74 20 74 68 65 20 70 61 74 68 77 61 79 20 66 6f 72 20 79 6f 75 72 20 71 75 69 63 6b 20 72 65 73 70 6f 6e 73 65 20 73 74 61 72 74 73 20 6e 65 61 72 20 6e 75 6d 65 72 61 63 79 20 61 6e 64 20 72 69 73 65 73 20 74 68 72 6f 75 67 68 20 6c 69 74 65 72 61 63 79"
msg_3 = msg_3.strip(" ")
msg_3 = hex_to_english_letters(msg_3)
print(f'hex letter: {msg_3}')