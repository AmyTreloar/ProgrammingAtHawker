from random import randint

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789?!., '
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
ENCRYPT = 0
DECRYPT = 1




def ceaser_cipher(msg,key,mode=ENCRYPT):
  out = ''
  translated_index = 0
  if mode == DECRYPT:
    key = 0 - key
  for symbol in msg:
    symbol = symbol.upper().strip()
    if symbol not in SYMBOLS:
      continue
    symbol_index = SYMBOLS.find(symbol)
    translated_index = symbol_index + key
    if translated_index >= len(SYMBOLS):
      translated_index -= len(SYMBOLS)
    elif translated_index < 0:
      translated_index += len(SYMBOLS)
    out += SYMBOLS[translated_index]
  return out

def ceaser_cipher_lean(msg, key, mode=ENCRYPT):
  out = ''
  translated_index = 0
  for symbol in msg:
    symbol = symbol.upper()
    if symbol not in SYMBOLS:
      continue
    symbol_index = SYMBOLS.find(symbol)
    # print(translated_index, symbol_index, key)
    if mode == ENCRYPT:
      translated_index = symbol_index + key
    elif mode == DECRYPT:
      translated_index = symbol_index - key
    # print(translated_index, symbol_index, key)
    if translated_index >= len(SYMBOLS):
      translated_index -= len(SYMBOLS)
    elif translated_index < 0:
      translated_index += len(SYMBOLS)
    out += SYMBOLS[translated_index]
    # print("-----")

  return out


# for key in range(len(LETTERS)):
tests = 0
count = 0
count_wins = 0
for j in range(100):
  print(".", end='')
  if tests % 10 == 0:
    print()
  tests += 1
  test_cipher = 'DPNQVUFSATDJFODFAJTAOPANPSFABCPVUADPNQVUFSTAUIBOABTUSPOPNZAJTABCPVUAUFMFTDPQFTAAFETHFSAX,AEJKLTUSB'
  message = "DPNQVUFSATDJFODFAJTAOPANPSFABCPVUADPNQVUFSTAUIBOABTUSPOPNZAJTABCPVUAUFMFTDPQFTAAFETHFSAX,AEJKLTUSB'"
  message = (message.replace(' ', ''))
  #key = randint(0,len(SYMBOLS))
  key = 1

  for i in range(100):
    for key in range(len(SYMBOLS)):
      plaintext2 = ceaser_cipher(message, key, DECRYPT)
      #print(key, '\t', plaintext2)
      if plaintext2[0] == "C":
        if plaintext2 != "COMPUTER SCIENCE IS NO MORE ABOUT COMPUTERS THAN ASTRONOMY IS ABOUT TELESCOPES  EDSGER W. DIJKSTRA":
          count+= 1
          print(tests, i, key, '\t', plaintext2, '\t', count)
        if plaintext2 == "COMPUTER SCIENCE IS NO MORE ABOUT COMPUTERS THAN ASTRONOMY IS ABOUT TELESCOPES  EDSGER W. DIJKSTRA":
          count_wins += 1

print(count_wins, count)
msg = 'adam'
msg_cipher_1 = 'BEBN'
print(ceaser_cipher(msg, 1) == msg_cipher_1)
print(test_cipher == message)
#   # print (message)
#   # print (cipher)
#   plaintext2 = ceaser_cipher(cipher2, key, DECRYPT)
#   print (' ')
#   print (key)
#   print (message)
#   print (cipher)
#   print (cipher2)
#   print (plaintext)
#   print (plaintext2)

#
# for i in range(1000000):
#   cipher = ceaser_cipher(message, key)
#   #cipher2 = ceaser_cipher_lean(message, key)
#   plaintext = ceaser_cipher(cipher, key, DECRYPT)
#   if cipher != test_cipher:
#     print("cipher broke: ", cipher, test_cipher)
#   if plaintext != message:
#     print("decipher broke: ", plaintext, message)