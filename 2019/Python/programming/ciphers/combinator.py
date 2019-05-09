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
    out = []
    for i in code:
        out.append(i)
    return out


def add_more_combos(new_combo, current_combo):
    if current_combo is None:
        current_combo = []
        for letter in new_combo:
            current_combo.append(letter)
        return current_combo

    out = []
    for cc in current_combo:
        for nc in new_combo:
            out.append(list(cc) + list(nc))
    return out


cipher = [2, 3, 2, 6]

matrix = None

for key in cipher:
    combo = get_letter_combos(keypad[key])
    matrix = add_more_combos(combo, matrix)

for text in matrix:
    print(''.join(text))
