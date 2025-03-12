from typing import List

def merge_sort(arr: List[int], left: int, right: int):
    """
    Sorts a portion of an array using the merge sort algorithm.

    Args:
        arr (List[int]): A list of integers that contains the elements to be sorted.
        left (int): The starting index of the portion of the array to be sorted.
        right (int): The ending index of the portion of the array to be sorted.

    Returns:

    """
    if left < right:
        middle = (left + right) // 2

        merge_sort(arr, left, middle)
        merge_sort(arr, middle + 1, right)

        merge(arr, left, middle, right)

def merge(arr: List[int], left: int, middle: int, right: int):
    left_subarray = arr[left:middle + 1]
    right_subarray = arr[middle + 1:right + 1]

    left_index = 0
    right_index = 0
    merged_index = left

    while left_index < len(left_subarray) and right_index < len(right_subarray):
        if left_subarray[left_index] < right_subarray[right_index]:
            arr[merged_index] = left_subarray[left_index]
            left_index += 1
        else:
            arr[merged_index] = right_subarray[right_index]
            right_index += 1
        merged_index += 1

    while left_index < len(left_subarray):
        arr[merged_index] = left_subarray[left_index]
        left_index += 1
        merged_index += 1

    while right_index < len(right_subarray):
        arr[merged_index] = right_subarray[right_index]
        right_index += 1
        merged_index += 1
import unittest


class Tester(unittest.TestCase):

    def test_sort_empty_array(self):
        """Test sorting an empty array."""
        empty_array = []
        merge_sort(empty_array, 0, len(empty_array) - 1)
        self.assertTrue(len(empty_array) == 0)  # Assert that the array is still empty

    def test_sort_single_element_array(self):
        """Test sorting a single element array."""
        single_element = [1]
        merge_sort(single_element, 0, len(single_element) - 1)
        self.assertEqual(single_element, [1])  # Assert that it remains the same

    def test_sort_sorted_array(self):
        """Test sorting a sorted array."""
        sorted_array = [1, 2, 3, 4, 5]
        merge_sort(sorted_array, 0, len(sorted_array) - 1)
        self.assertEqual(sorted_array, [1, 2, 3, 4, 5])  # Correct the expected value

    def test_sort_reverse_sorted_array(self):
        """Test sorting a reverse sorted array."""
        reverse_sorted_array = [5, 4, 3, 2, 1]
        merge_sort(reverse_sorted_array, 0, len(reverse_sorted_array) - 1)
        self.assertEqual(reverse_sorted_array, [1, 2, 3, 4, 5])  # Assert it sorts correctly

    def test_sort_random_integers(self):
        """Test sorting an array with random integers."""
        random_array = [38, 27, 43, 3, 9, 82, 10]
        expected_sorted_array = [3, 9, 10, 27, 38, 43, 82]
        merge_sort(random_array, 0, len(random_array) - 1)
        self.assertEqual(random_array, expected_sorted_array)  # Assert the sorted array is correct

if __name__ == '__main__':
    unittest.main()