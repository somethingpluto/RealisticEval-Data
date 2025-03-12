from typing import List

def adjust_array_length(target_length: int, array: List) -> List:
    """
    Adjust the length of the input array according to the given target length.
    If the current length of the array is longer than the target length,
    the first part of the array is intercepted to match the target length.
    If the current length of the array is shorter than the target length,
    the elements in the array are repeated until the target length is reached.

    Args:
        target_length (int): The desired length for the array.
        array (List): The input array to be adjusted.

    Returns:
        List: A new array that has been adjusted to the target length.
    """
    current_length = len(array)
    
    if current_length > target_length:
        return array[:target_length]
    elif current_length < target_length:
        repetitions = target_length // current_length
        remainder = target_length % current_length
        return (array * repetitions) + array[:remainder]
    else:
        return array
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