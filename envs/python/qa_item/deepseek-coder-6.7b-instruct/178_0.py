from typing import List

def find_longest_non_decreasing_subsequence(nums: List[int]) -> List[int]:
    """Find the longest non-decreasing subsequence in the given list.

    Args:
        nums (List[int]): The input array of integers.

    Returns:
        List[int]: A list containing the longest non-decreasing subsequence.
    """
    if not nums:
        return []

    n = len(nums)
    dp = [1] * n
    prev = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] >= nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j

    # Find the index of the maximum value in dp
    max_len = max(dp)
    max_index = dp.index(max_len)

    # Reconstruct the longest non-decreasing subsequence
    result = []
    while max_index != -1:
        result.append(nums[max_index])
        max_index = prev[max_index]

    return result[::-1]
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