
from typing import List

def min_removals_to_make_unique(nums: List[int]) -> int:
    """
    Given an integer array, calculate the minimum number of elements to delete so that the elements in the array are not duplicate.
    For example:
        input: [3, 3, 1, 2, 2, 1]
        output: 3

    Args:
        nums (List[int]): integer array of nums

    Returns:
        minimum number of moves to make every value in nums unique
    """
    # Calculate the number of unique values in the input array
    num_unique = sum([nums[i] for i in range(len(nums))])

    # Calculate the number of removed elements
    num_ Removals = len(nums) - num_unique

    return num_ Removals

import unittest


class TestMinRemovalsToMakeUnique(unittest.TestCase):
    def test_basic_array(self):
        """Test with a basic array where multiple removals are needed."""
        self.assertEqual(min_removals_to_make_unique([3, 3, 1, 2, 2, 1]), 3)

    def test_all_identical(self):
        """Test an array where all elements are identical."""
        self.assertEqual(min_removals_to_make_unique([4, 4, 4, 4]), 3)

    def test_all_unique(self):
        """Test an array where all elements are already unique."""
        self.assertEqual(min_removals_to_make_unique([1, 2, 3, 4]), 0)

    def test_empty_array(self):
        """Test an empty array."""
        self.assertEqual(min_removals_to_make_unique([]), 0)

    def test_complex_case(self):
        """Test a more complex case with a larger array."""
        self.assertEqual(min_removals_to_make_unique([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]), 6)
if __name__ == '__main__':
    unittest.main()