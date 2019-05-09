# import itertools



# def possible_words(phone_number):
#     letters_to_combine = (letters_map[digit] for digit in phone_number)
#     for letters_group in itertools.product(*letters_to_combine):
#         yield ''.join(letters_group)

# print(list(possible_words('2326')))





letters_map = {'2':'ABC', '3':'DEF', '4':'GHI', '5':'JKL', 
               '6':'MNO', '7':'PQRS', '8':'TUV', '9':'WXYZ'}


phone_number = ['2','3','2', '6']

# def stuff(s = ''):
#     if s == "true":
#         return "yay"
#     s = input("write words")
#     return stuff(s)
# stuff()
for i in range(len(letters_map['2'])):
    first_letter = letters_map['2'][i]
    for j in range(len(letters_map['3'])):
        second_letter = letters_map['3'][j]
        for k in range(len(letters_map['2'])):
            third_letter = letters_map['2'][k]
            for l in range(len(letters_map['6'])):
                fourth_letter = letters_map['6'][l]
                print(f'{first_letter}{second_letter}{third_letter}{fourth_letter}')
    










