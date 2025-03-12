from typing import List

def next_greatest_letter(letters: List[str], target: str) -> str:
    i = 0
    j = len(letters) - 1
    
    while i <= j:
        mid = i + (j - i) // 2
        if letters[mid] <= target:
            i = mid + 1
        else:
            j = mid - 1
    
    return letters[i % len(letters)] if i < len(letters) else letters[0]
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
if __name__ == '__main__':
    unittest.main()