from typing import List
import math

def calculate(values: List[int], period: int) -> float:
    if not values or period <= 0:
        return math.nan
    if period > len(values):
        return math.nan
    return sum(values[-period:]) / period
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