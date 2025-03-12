from typing import List

def adjust_array_length(target_length: int, array: List) -> List:
    while len(array) < target_length:
        array += array[:target_length - len(array)]
    return array[:target_length]
import unittest


class TestAdjustArrayLength(unittest.TestCase):

    def test_array_length_equal_to_target_length(self):
        result = adjust_array_length(5, [1, 2, 3, 4, 5])
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_array_length_shorter_than_target_length(self):
        result = adjust_array_length(8, [1, 2, 3])
        self.assertEqual(result, [1, 2, 3, 1, 2, 3, 1, 2])

    def test_array_length_shorter_than_target_length_multiple(self):
        result = adjust_array_length(6, [10, 20])
        self.assertEqual(result, [10, 20, 10, 20, 10, 20])

    def test_array_length_shorter_than_target_length_not_multiple(self):
        result = adjust_array_length(7, [7, 14, 21])
        self.assertEqual(result, [7, 14, 21, 7, 14, 21, 7])

if __name__ == '__main__':
    unittest.main()