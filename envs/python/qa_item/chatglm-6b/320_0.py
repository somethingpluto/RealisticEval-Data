
from typing import List

def get_array_average(array: List[float]) -> float:
    """
    Calculate the average of an array of numbers.
    Args:
        array (List[float]): A list of numbers for which the average is to be calculated.

    Returns:
        float: The average (mean) of the array's elements, or float('nan') if the array is empty.
    """
    if len(array) == 0:
        return float('nan')
    else:
        return sum(array) / len(array)

import math
import unittest


class TestGetArrayAverage(unittest.TestCase):

    def test_average_of_positive_integers(self):
        result = get_array_average([1, 2, 3, 4, 5])
        self.assertEqual(result, 3)  # (1 + 2 + 3 + 4 + 5) / 5 = 3

    def test_average_with_negative_numbers(self):
        result = get_array_average([-1, -2, -3, -4, -5])
        self.assertEqual(result, -3)  # (-1 + -2 + -3 + -4 + -5) / 5 = -3

    def test_average_with_mixed_numbers(self):
        result = get_array_average([1, -1, 2, -2, 3, -3])
        self.assertEqual(result, 0)  # (1 + -1 + 2 + -2 + 3 + -3) / 6 = 0


    def test_single_element_array(self):
        result = get_array_average([7])
        self.assertEqual(result, 7)  # The average of [7] is 7

if __name__ == '__main__':
    unittest.main()