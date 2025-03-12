
from typing import List

def length_of_LIS(nums: List[int]) -> int:
    """
    Given an array of integers nums, find the length of the longest strictly increasing subsequence in it

    Args:
        nums (List[int]): int array

    Returns:
        int: longest strictly increasing subsequence
    """
    # Iterate over the array and find the first index where the current element is greater than the last element
    # This will give us the start and end indices of the strictly increasing subsequence
    start = 0
    end = len(nums) - 1
    while start < end:
        # If the current element is greater than the last element, we have found a strictly increasing subsequence
        if nums[end] > nums[start]:
            end = start
        else:
            # Increment the start index if the current element is smaller
            start += 1
    # Calculate the length of the strictly increasing subsequence
    return end - start

import unittest
from typing import List

class TestLengthOfLIS(unittest.TestCase):

    def test_empty_list(self):
        # Test the function with an empty list
        self.assertEqual(length_of_LIS([]), 0)

    def test_single_element(self):
        # Test with a list containing only one element
        self.assertEqual(length_of_LIS([7]), 1)

    def test_increasing_sequence(self):
        # Test with a list where the elements are strictly increasing
        self.assertEqual(length_of_LIS([1, 2, 3, 4, 5]), 5)

    def test_decreasing_sequence(self):
        # Test with a list where the elements are strictly decreasing
        self.assertEqual(length_of_LIS([5, 4, 3, 2, 1]), 1)

    def test_complex_sequence(self):
        # Test with a complex sequence with mix of increasing and decreasing elements
        self.assertEqual(length_of_LIS([10, 9, 2, 5, 3, 7, 101, 18]), 4)

    def test_all_equal_elements(self):
        # Test with all elements in the list being equal
        self.assertEqual(length_of_LIS([2, 2, 2, 2]), 1)

    def test_with_negative_numbers(self):
        # Test with a mix of negative and positive numbers
        self.assertEqual(length_of_LIS([-1, -2, -3, 0, 1, 2]), 4)
if __name__ == '__main__':
    unittest.main()