from typing import List

def calculate_average_difference(numbers: List[int]) -> float:
    """Calculates the average difference between consecutive integers in the provided list.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        float: The average difference between consecutive integers, or 0 if there are fewer than 2 integers.
    """
    if len(numbers) < 2:
        return 0.0
    
    differences = [abs(numbers[i] - numbers[i - 1]) for i in range(1, len(numbers))]
    average_difference = sum(differences) / len(differences)
    
    return average_difference
import unittest
from typing import List


class TestCalculateAverageDifference(unittest.TestCase):

    def test_calculate_average_difference_positive_integers(self):
        numbers: List[int] = [10, 20, 30, 40]
        result = calculate_average_difference(numbers)
        expected = 10.0
        self.assertAlmostEqual(expected, result, msg="The average difference should be 10.0")

    def test_calculate_average_difference_mixed_positive_and_negative(self):
        numbers: List[int] = [-10, 0, 10, 20]
        result = calculate_average_difference(numbers)
        expected = 10.0
        self.assertAlmostEqual(expected, result, msg="The average difference should be 10.0")

    def test_calculate_average_difference_same_values(self):
        numbers: List[int] = [5, 5, 5, 5]
        result = calculate_average_difference(numbers)
        expected = 0.0
        self.assertAlmostEqual(expected, result, msg="The average difference should be 0.0 as all values are the same")

    def test_calculate_average_difference_single_element(self):
        numbers: List[int] = [100]
        result = calculate_average_difference(numbers)
        expected = 0.0  # Not enough data to calculate differences
        self.assertAlmostEqual(expected, result, msg="The average difference should be 0.0 for a single element list")

    def test_calculate_average_difference_empty_list(self):
        numbers: List[int] = []
        result = calculate_average_difference(numbers)
        expected = 0.0  # Not enough data to calculate differences
        self.assertAlmostEqual(expected, result, msg="The average difference should be 0.0 for an empty list")
if __name__ == '__main__':
    unittest.main()