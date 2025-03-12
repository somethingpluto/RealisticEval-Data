from typing import List

def insertion_sort(arr: List):
    """
    Sorts a list of floats in ascending order using the insertion sort algorithm.

    Args:
        arr (List): The list of floats to be sorted.

    Returns:
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
import unittest


class TestAnswer(unittest.TestCase):
    def test_basic_unsorted_array(self):
        """Test case 1: Basic unsorted array."""
        arr = [12.4, 11.2, 13.5, 5.6, 6.7]
        expected = [5.6, 6.7, 11.2, 12.4, 13.5]
        insertion_sort(arr)
        self.assertEqual(expected, arr)

    def test_already_sorted_array(self):
        """Test case 2: Already sorted array."""
        arr = [1.1, 2.2, 3.3, 4.4, 5.5]
        expected = [1.1, 2.2, 3.3, 4.4, 5.5]
        insertion_sort(arr)
        self.assertEqual(expected, arr)

    def test_reverse_sorted_array(self):
        """Test case 3: Reverse sorted array."""
        arr = [5.5, 4.4, 3.3, 2.2, 1.1]
        expected = [1.1, 2.2, 3.3, 4.4, 5.5]
        insertion_sort(arr)
        self.assertEqual(expected, arr)

    def test_empty_array(self):
        """Test case 4: Empty array."""
        arr = []
        expected = []
        insertion_sort(arr)
        self.assertEqual(expected, arr)

    def test_single_element_array(self):
        """Test case 5: Single element array."""
        arr = [3.3]
        expected = [3.3]
        insertion_sort(arr)
        self.assertEqual(expected, arr)

    def test_array_with_duplicates(self):
        """Test case 6: Array with duplicate values."""
        arr = [2.2, 3.3, 2.2, 1.1, 3.3]
        expected = [1.1, 2.2, 2.2, 3.3, 3.3]
        insertion_sort(arr)
        self.assertEqual(expected, arr)

    def test_large_numbers(self):
        """Test case 7: Large numbers."""
        arr = [1e10, 1e9, 1e11, 1e8]
        expected = [1e8, 1e9, 1e10, 1e11]
        insertion_sort(arr)
        self.assertEqual(expected, arr)

if __name__ == '__main__':
    unittest.main()