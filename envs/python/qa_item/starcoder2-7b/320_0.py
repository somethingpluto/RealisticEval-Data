from typing import List

def get_array_average(array: List[float]) -> float:
    if len(array) == 0:
        return float('nan')
    return sum(array) / len(array)
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

    def test_empty_array(self):
        result = get_array_average([])
        self.assertTrue(math.isnan(result))  # Division by zero, expected result is NaN

    def test_single_element_array(self):
        result = get_array_average([7])
        self.assertEqual(result, 7)  # The average of [7] is 7

if __name__ == '__main__':
    unittest.main()