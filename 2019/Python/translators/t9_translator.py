t9code = {
    2: "abc",
    3: "def",
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
}
cipher = [2, 3, 2, 6]
#code = [7, 7, 6, 4, 2, 6, 6, 4, 6, 4]

possible_combos = []

from itertools import permutations
combos = []
for number in cipher:
    letters = t9code[number]
    i = 0
    for perm in permutations(list(letters)):
        combos.append([])
        i += 1
        print(combos)
        for letter in range(len(perm)):
            print(perm[letter])
            if len(combos) < i+1:
                combos[i].append([])
                print(combos)
            combos[i].append(perm[letter])
print(combos)
# for perm in permutations(list(t9code[2])):
#     print(perm, len(perm))

# for num in code:
#     print(t9code[num])
#     combos.append( permutations(list(t9code[num])))
# for combo in combos:
#     print(len(combo))
#     for c in combo:
#         print(len(c))
#         print(c)
# perm = permutations(combos)
# print(list(perm)[:2])
# for i in range(len(combos)):
#     word = combos[i]
#     for j in range(len(word)):
#         print(word[j], end=' ')
#     print()

