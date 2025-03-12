
from typing import List

def find_longest_non_decreasing_subsequence(nums: List[int]) -> List[int]:
    """Find the longest non-decreasing subsequence in the given list.

    Args:
        nums (List[int]): The input array of integers.

    Returns:
        List[int]: A list containing the longest non-decreasing subsequence.
    """
    # Iterate over the list and find the first non-decreasing subsequence
    first_non_decreasing = [x for x in nums if not nums[x - 1] > nums[x]]
    # Iterate over the list and find the last non-decreasing subsequence
    last_non_decreasing = [x for x in nums if not nums[-1] < nums[x]]
    # Return the list of non-decreasing subsequences
    return first_non_decreasing, last_non_decreasing

import unittest
from typing import List


class TestAnswer(unittest.TestCase):

    def test_non_decreasing_sequence(self):
        nums = [5, 7, 4, 8, 6, 10, 2, 11]
        expected: List[int] = [5, 7, 8, 10, 11]
        self.assertEqual(expected, find_longest_non_decreasing_subsequence(nums))

    def test_all_increasing(self):
        nums = [1, 2, 3, 4, 5]
        expected: List[int] = [1, 2, 3, 4, 5]
        self.assertEqual(expected, find_longest_non_decreasing_subsequence(nums))

    def test_all_decreasing(self):
        nums = [5, 4, 3, 2, 1]
        expected: List[int] = [5]
        self.assertEqual(expected, find_longest_non_decreasing_subsequence(nums))

    def test_single_element(self):
        nums = [10]
        expected: List[int] = [10]
        self.assertEqual(expected, find_longest_non_decreasing_subsequence(nums))

    def test_empty_array(self):
        nums = []
        expected: List[int] = []
        self.assertEqual(expected, find_longest_non_decreasing_subsequence(nums))
if __name__ == '__main__':
    unittest.main()