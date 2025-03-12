from typing import List

def length_of_LIS(nums: List[int]) -> int:
    dp = [1] * len(nums)

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp) if dp else 0
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