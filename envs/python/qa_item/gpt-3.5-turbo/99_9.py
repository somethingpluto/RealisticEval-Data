from typing import List

def calculate_sum(arr: List[int]):
    total = sum(arr)
    return total
import unittest


class TestSumFunction(unittest.TestCase):

    def test_sum_of_positive_numbers(self):
        """Test the sum of a normal array of positive numbers."""
        self.assertEqual(calculate_sum([1, 2, 3, 4, 5]), 15)

    def test_sum_of_negative_numbers(self):
        """Test the sum of an array containing negative numbers."""
        self.assertEqual(calculate_sum([-1, -2, -3, -4, -5]), -15)

    def test_sum_of_empty_array(self):
        """Test that the sum of an empty array is 0."""
        self.assertEqual(calculate_sum([]), 0)

    def test_sum_of_mixed_numbers(self):
        """Test the sum of an array containing both positive and negative numbers."""
        self.assertEqual(calculate_sum([10, -10, 5, -5, 15]), 15)

    def test_sum_of_floating_point_numbers(self):
        """Test the sum of an array with floating point numbers."""
        self.assertAlmostEqual(calculate_sum([1.5, 2.5, 3.5]), 7.5)

if __name__ == '__main__':
    unittest.main()