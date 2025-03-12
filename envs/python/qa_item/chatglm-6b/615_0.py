
from typing import List

def calculate(values: List[int], period: int) -> float:
    if period <= 0:
        raise ValueError("Invalid period")
    
    last_period = len(values) - period
    
    if not values:
        raise ValueError("Input list does not contain enough elements")
    
    return sum(values[:last_period]) / last_period

# Example usage
values = [1, 2, 3, 4, 5]
period = 3
print(calculate(values, period))  # Output: 1.5

import math
import unittest


class TestAnswer(unittest.TestCase):

    def test_calculate_with_valid_input(self):
        values = [1, 2, 3, 4, 5]
        period = 3
        expected = 4.0  # (3 + 4 + 5) / 3
        self.assertEqual(expected, calculate(values, period))

    def test_calculate_with_all_same_values(self):
        values = [5, 5, 5, 5, 5]
        period = 5
        expected = 5.0  # (5 + 5 + 5 + 5 + 5) / 5
        self.assertEqual(expected, calculate(values, period))

    def test_calculate_with_single_value(self):
        values = [10]
        period = 1
        expected = 10.0  # (10) / 1
        self.assertEqual(expected, calculate(values, period))

    def test_calculate_with_insufficient_values(self):
        values = [1, 2]
        period = 3
        self.assertTrue(math.isnan(calculate(values, period)))  # Expecting NaN

    def test_calculate_with_empty_list(self):
        values = []
        period = 1
        self.assertTrue(math.isnan(calculate(values, period)))  # Expecting NaN

    def test_calculate_with_negative_period(self):
        values = [1, 2, 3, 4, 5]
        period = -1
        self.assertTrue(math.isnan(calculate(values, period)))  # Expecting NaN
if __name__ == '__main__':
    unittest.main()