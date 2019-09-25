import unittest

def check_for_3_vowels(string_in):
    vowels = 'aeiou'
    count = 0
    for v in vowels:
        count += string_in.count(v)

    if count >= 3:
        return True
    return False

def check_for_no_banned_combos(string_in):
    banned = ['ab', 'cd', 'pq', 'xy']
    count = 0
    for b in banned:
        count += string_in.count(b)
        if count>= 1:
            return False
    return True

def check_for_no_doubled_letters(string_in):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    dict_alpha = {}
    for a in alpha:
        if a in dict_alpha:
            dict_alpha[a] += 1
        else:
            dict_alpha[a] = 0
    for s in string_in:
        if s in dict_alpha:
            dict_alpha[s] += 1
        else:
            dict_alpha[s] = 1
    for da in dict_alpha:
        if dict_alpha[da] > 1: 
            return False
    return True

def check_naughty(string_in):
    return check_for_3_vowels(string_in) and check_for_no_banned_combos(string_in) and check_for_no_doubled_letters(string_in)

class TestPastFrames(unittest.TestCase):
    def test_3_vowels(self):
        self.assertTrue(check_for_3_vowels('aie'))
        self.assertTrue(check_for_3_vowels('aaa'))
        self.assertTrue(check_for_3_vowels('xazegov'))
        self.assertTrue(check_for_3_vowels('aeiouaeiouaeiou'))
        self.assertTrue(check_for_3_vowels('ugknbfddgicrmopn'))
        self.assertFalse(check_for_3_vowels('bnm'))
        self.assertFalse(check_for_3_vowels('ain'))

    def test_for_banned_combos(self):
        self.assertFalse(check_for_no_banned_combos('ab'))
        self.assertTrue(check_for_no_banned_combos('xx'))
        self.assertFalse(check_for_no_banned_combos('abcdde'))
        self.assertFalse(check_for_no_banned_combos('aabbccdd'))
        self.assertTrue(check_for_no_banned_combos('aaa'))

    def test_for_no_double_letters(self):
        self.assertFalse(check_for_no_doubled_letters('aa'))
        self.assertTrue(check_for_no_doubled_letters('ab'))
        self.assertFalse(check_for_no_doubled_letters('xx'))
        self.assertFalse(check_for_no_doubled_letters('abcdde'))
        self.assertFalse(check_for_no_doubled_letters('aabbccdd'))

    def test_check_nice(self):
        self.assertTrue(check_naughty('ugknbfddgicrmopn'))
        self.assertTrue(check_naughty('aaa'))
        self.assertFalse(check_naughty('jchzalrnumimnmhp'))
        self.assertFalse(check_naughty('haegwjzuvuyypxyu'))
        self.assertFalse(check_naughty('dvszwmarrgswjxmb'))

if __name__ == '__main__':
    unittest.main() 