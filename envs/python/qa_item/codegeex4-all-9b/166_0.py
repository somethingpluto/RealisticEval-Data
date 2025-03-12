from typing import List

def next_greatest_letter(letters: List[str], target: str) -> str:
    """
    Finds and returns the smallest letter in a sorted array that is larger than the given target letter.
    If the target letter is greater than or equal to all letters in the array, the function returns
    the first letter in the array.

    Args:
        letters (List[str]): A sorted array of letters (assumed to be unique and lowercase).
        target (str): The target letter to find the next greatest letter for.

    Returns:
        str: The smallest letter in the array that is larger than the target letter.
             If the target is greater than or equal to all letters, returns the first letter in the array.
    """
    n = len(letters)
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if letters[mid] > target:
            right = mid
        else:
            left = mid + 1
    return letters[left % n]
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