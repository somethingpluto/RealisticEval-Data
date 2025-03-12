from typing import List

def find_longest_non_decreasing_subsequence(nums: List[int]) -> List[int]:
    if not nums:
        return []
    
    n = len(nums)
    dp = [1] * n
    prev = [-1] * n
    max_len = 1
    max_index = 0

    for i in range(1, n):
        for j in range(i):
            if nums[i] >= nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
                if dp[i] > max_len:
                    max_len = dp[i]
                    max_index = i

    longest_sequence = []
    while max_index != -1:
        longest_sequence.insert(0, nums[max_index])
        max_index = prev[max_index]

    return longest_sequence
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