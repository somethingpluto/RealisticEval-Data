from typing import List

def find_longest_non_decreasing_subsequence(nums: List[int]) -> List[int]:
    longest_subsequence = []
    seq_length = [1] * len(nums)
    prev_index = [-1] * len(nums)
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] >= nums[j] and seq_length[i] < seq_length[j] + 1:
                seq_length[i] = seq_length[j] + 1
                prev_index[i] = j
    
    max_length = max(seq_length)
    max_index = seq_length.index(max_length)
    
    while max_index != -1:
        longest_subsequence.insert(0, nums[max_index])
        max_index = prev_index[max_index]
    
    return longest_subsequence
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