from itertools import groupby

def look_and_say(number: str):
    next_number = ''
    for digit, group in groupby(number):
        count = len(list(group))
        next_number += str(count) + digit
    return next_number
import unittest

class TestLookAndSay(unittest.TestCase):

    def test_single_digit(self):
        # Test with a single digit to see if it replicates correctly
        self.assertEqual(look_and_say('1'), '11')

    def test_repetitive_digits(self):
        # Test a sequence of the same digits
        self.assertEqual(look_and_say('111'), '31')

    def test_mixed_digits(self):
        # Test a sequence with different digits
        self.assertEqual(look_and_say('1211'), '111221')

    def test_complex_sequence(self):
        # Test a more complex sequence
        self.assertEqual(look_and_say('312211'), '13112221')

if __name__ == '__main__':
    unittest.main()