from typing import List

def filter_out_even_numbers(array: List[int]) -> List[int]:
    """
    Filters out all even numbers from an array.

    Args:
        array (List[int]): The array of numbers to filter.

    Returns:
        List[int]: A new array containing only the odd numbers.
    """

    return [num for num in array if num % 2 != 0]
import unittest


class TestFilterOutEvenNumbers(unittest.TestCase):

    def test_removes_all_even_numbers_from_the_array(self):
        input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = filter_out_even_numbers(input_array)
        self.assertEqual(result, [1, 3, 5, 7, 9])

    def test_returns_empty_array_when_input_is_empty(self):
        input_array = []
        result = filter_out_even_numbers(input_array)
        self.assertEqual(result, [])

    def test_returns_same_array_if_all_numbers_are_odd(self):
        input_array = [1, 3, 5, 7, 9]
        result = filter_out_even_numbers(input_array)
        self.assertEqual(result, [1, 3, 5, 7, 9])

    def test_returns_empty_array_if_all_numbers_are_even(self):
        input_array = [2, 4, 6, 8, 10]
        result = filter_out_even_numbers(input_array)
        self.assertEqual(result, [])

    def test_handles_mixed_positive_and_negative_numbers(self):
        input_array = [-3, -2, -1, 0, 1, 2, 3]
        result = filter_out_even_numbers(input_array)
        self.assertEqual(result, [-3, -1, 1, 3])

    def test_handles_large_numbers_and_zero_correctly(self):
        input_array = [0, 1000000000, 1000000001, 1000000002, 1000000003]
        result = filter_out_even_numbers(input_array)
        self.assertEqual(result, [1000000001, 1000000003])

if __name__ == '__main__':
    unittest.main()