from typing import List

def find_longest_non_decreasing_subsequence(nums: List[int]) -> List[int]:
    # Initialize variables to store the length of the input list and the maximum length of the subsequence
    n = len(nums)
    lis = [1] * n
    
    # Initialize the parent array to track the previous element in the longest subsequence
    parent = [-1] * n
    
    # Iterate over the elements in the input list
    for i in range(1, n):
        for j in range(0, i):
            if nums[i] >= nums[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
                parent[i] = j
    
    # Find the index of the maximum value in lis
    max_index = 0
    for i in range(n):
        if lis[i] > lis[max_index]:
            max_index = i
    
    # Reconstruct the longest non-decreasing subsequence using the parent array
    result = []
    while max_index != -1:
        result.append(nums[max_index])
        max_index = parent[max_index]
    
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