from typing import List

def length_of_LIS(nums: List[int]) -> int:
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

    max_len = max(dp)
    return max_len
import unittest


class TestLengthOFLIS(unittest.TestCase):
    def test_case_1(self):
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        expected = 4
        self.assertEqual(length_of_LIS(nums), expected)

    def test_case_2(self):
        nums = [0, 1, 0, 3, 2, 3]
        expected = 4
        self.assertEqual(length_of_LIS(nums), expected)

    def test_case_3(self):
        nums = [7, 7, 7, 7, 7, 7, 7]
        expected = 1
        self.assertEqual(length_of_LIS(nums), expected)

if __name__ == '__main__':
    unittest.main()