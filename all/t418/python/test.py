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
