import unittest


class TestNextGreatestLetter(unittest.TestCase):

    def test_target_greater_than_all_letters(self):
        letters = ['c', 'f', 'j']
        target = 'j'
        result = next_greatest_letter(letters, target)
        self.assertEqual(result, 'c')  # Expected output: 'c'

    def test_typical_input(self):
        letters = ['c', 'f', 'j']
        target = 'a'
        result = next_greatest_letter(letters, target)
        self.assertEqual(result, 'c')  # Expected output: 'c'

    def test_edge_case_between_two_letters(self):
        letters = ['c', 'f', 'j']
        target = 'd'
        result = next_greatest_letter(letters, target)
        self.assertEqual(result, 'f')  # Expected output: 'f'

    def test_target_equal_to_largest_letter(self):
        letters = ['a', 'b', 'c', 'd']
        target = 'd'
        result = next_greatest_letter(letters, target)
        self.assertEqual(result, 'a')  # Expected output: 'a'

    def test_single_letter_array(self):
        letters = ['a']
        target = 'z'
        result = next_greatest_letter(letters, target)
        self.assertEqual(result, 'a')  # Expected output: 'a'