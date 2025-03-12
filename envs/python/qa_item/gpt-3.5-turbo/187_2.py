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
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    left_arr = [0] * n1
    right_arr = [0] * n2

    for i in range(n1):
        left_arr[i] = arr[left + i]

    for j in range(n2):
        right_arr[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right_arr[j]
        j += 1
        k += 1
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