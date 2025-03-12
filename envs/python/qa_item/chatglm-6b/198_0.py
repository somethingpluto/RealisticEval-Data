
from typing import List

def find_max_difference(l: List[int]) -> int:
    """
    Finds the maximum difference between elements in the array such that the smaller element appears before the larger one.
    Args:
        l (List[int]): A list of integers containing the elements.

    Returns:
        int: The maximum difference.
    """
    # Iterate over the list and compare the smaller and larger elements
    for i in range(len(l)):
        if l[i] < l[i+1]:
            # Calculate the difference between the two elements
            diff = l[i] - l[i+1]
            # If the difference is negative, it means the smaller element is earlier
            if diff < 0:
                # Set the maximum difference to the absolute value of the difference
                max_diff = abs(diff)
            else:
                # If the difference is positive, it means the larger element is earlier
                max_diff = diff
    return max_diff

import unittest


class Tester(unittest.TestCase):

    def test_general_case(self):
        l = [2, 3, 10, 6, 4, 8, 1]
        self.assertEqual(find_max_difference(l), 8)  # Maximum difference is 10 - 2 = 8

    def test_decreasing_sequence(self):
        l = [10, 9, 8, 7, 6, 5]
        self.assertEqual(find_max_difference(l), 0)  # Maximum difference should be 0

    def test_all_elements_same(self):
        l = [5, 5, 5, 5, 5]
        self.assertEqual(find_max_difference(l), 0)  # Maximum difference is 5 - 5 = 0

    def test_only_two_elements(self):
        l = [3, 8]
        self.assertEqual(find_max_difference(l), 5)  # Maximum difference is 8 - 3 = 5

    def test_single_element(self):
        l = [4]
        self.assertEqual(find_max_difference(l), 0)  # Only one element, no difference to calculate

if __name__ == '__main__':
    unittest.main()