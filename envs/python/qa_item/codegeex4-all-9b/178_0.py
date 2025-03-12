from typing import List

def find_longest_non_decreasing_subsequence(nums: List[int]) -> List[int]:
    if not nums:
        return []
    
    # Initialize the lists to store the best end element and the length of the subsequence
    best_end = [nums[0]]
    lengths = [1]
    
    for num in nums[1:]:
        if num >= best_end[-1]:
            best_end.append(num)
            lengths.append(lengths[-1] + 1)
        else:
            # Binary search to find the first element in best_end that is greater than or equal to num
            low, high = 0, len(best_end) - 1
            while low < high:
                mid = (low + high) // 2
                if best_end[mid] < num:
                    low = mid + 1
                else:
                    high = mid
            best_end[low] = num
            lengths.append(lengths[low])
    
    # Reconstruct the longest non-decreasing subsequence
    max_length = max(lengths)
    index = lengths.index(max_length)
    longest_subseq = [best_end[index]]
    for num in reversed(nums):
        if lengths[index] == 1:
            break
        if best_end[index - 1] <= num:
            longest_subseq.append(num)
            index -= 1
    longest_subseq.reverse()
    
    return longest_subseq
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