from typing import List

def find_median(arr: List[int]) -> float:
    """
    Finds the median of a given array of numbers.

    Args:
        arr (list of int): The array of numbers to find the median of.

    Returns:
        float: The median of the array.
    """
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    
    if n % 2 == 1:
        return sorted_arr[n // 2]
    else:
        mid1 = sorted_arr[n // 2 - 1]
        mid2 = sorted_arr[n // 2]
        return (mid1 + mid2) / 2
import random
import unittest


class TestFindMedian(unittest.TestCase):

    # Test Case 1: Check median for large array
    def test_large_array_median(self):
        large_array = [random.randint(0, 9999) for _ in range(10001)]
        median_large_array = find_median(large_array)
        # Test passes if the median is a number
        self.assertIsInstance(median_large_array, (int, float))

    # Test Case 2: Odd number of elements
    def test_odd_number_of_elements(self):
        arr = [3, 1, 4, 1, 5, 9, 2]
        median = find_median(arr)
        self.assertEqual(median, 3)

    # Test Case 3: Even number of elements
    def test_even_number_of_elements(self):
        arr = [10, 2, 3, 5, 7, 8]
        median = find_median(arr)
        self.assertEqual(median, 6)

    # Test Case 4: Array with duplicate elements
    def test_array_with_duplicates(self):
        arr = [1, 2, 2, 2, 3]
        median = find_median(arr)
        self.assertEqual(median, 2)

    # Test Case 5: Array with negative numbers
    def test_array_with_negative_numbers(self):
        arr = [-5, -10, 0, 5, 10]
        median = find_median(arr)
        self.assertEqual(median, 0)

    # Test Case 6: Array with a single element
    def test_single_element_array(self):
        arr = [42]
        median = find_median(arr)
        self.assertEqual(median, 42)

if __name__ == '__main__':
    unittest.main()