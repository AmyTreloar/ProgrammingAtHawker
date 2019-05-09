keypad = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
}


def get_letter_combos(code):
    """breaks up each string into a list of characters"""
    out = []
    for i in code:
        out.append(i)
    return out


def add_more_combos(new_combo, current_combo):
    """creates a matrix of different combinations for each new combination"""
    #If there is nothing in the matrix so far create it
    if current_combo is None:
        current_combo = []
        for letter in new_combo:
            current_combo.append(letter)
        #then return it
        return current_combo

    #If the matrix has been created previously add to it. 
    out = []
    for cc in current_combo:
        for nc in new_combo:
            #add the current combo to each new combo
            out.append(list(cc) + list(nc))
    return out

#this is the input code
cipher = [2, 3, 2, 6]

#we don't have a matrix yet
matrix = None

for key in cipher:
    combo = get_letter_combos(keypad[key]) #get the combo
    matrix = add_more_combos(combo, matrix) #add it to the matrix

#print the matrix as words
for text in matrix:
    print(''.join(text))