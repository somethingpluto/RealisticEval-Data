from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Finds two indices of numbers in the array that sum up to the target value.

    Args:
        nums (List[int]): The input array of integers.
        target (int): The target sum value.

    Returns:
        list[int]: A list containing the indices of the two numbers.

    Raises:
        ValueError: If no such indices are found.
    """
    num_to_index = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in num_to_index:
            return [num_to_index[complement], i]
        
        num_to_index[num] = i
    
    raise ValueError("No two indices found that sum up to the target value")
import unittest


class TestAnswer(unittest.TestCase):
    def test_valid_pair(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]  # 2 + 7 = 9
        self.assertEqual(expected, two_sum(nums, target))

    def test_negative_numbers(self):
        nums = [-1, -2, -3, -4, -5]
        target = -8
        expected = [2, 4]  # -3 + -5 = -8
        self.assertEqual(expected, two_sum(nums, target))

    def test_zero_sum(self):
        nums = [0, 4, 3, 0]
        target = 0
        expected = [0, 3]  # 0 + 0 = 0
        self.assertEqual(expected, two_sum(nums, target))

    def test_no_solution(self):
        nums = [1, 2, 3, 4, 5]
        target = 10
        with self.assertRaises(Exception):
            two_sum(nums, target)

    def test_same_number_twice(self):
        nums = [3, 3]
        target = 6
        expected = [0, 1]  # 3 + 3 = 6
        self.assertEqual(expected, two_sum(nums, target))

    def test_large_numbers(self):
        nums = [2147483647, -2147483648, 0, 1]
        target = 1
        expected = [2, 3]  # 0 + 1 = 1
        self.assertEqual(expected, two_sum(nums, target))
if __name__ == '__main__':
    unittest.main()