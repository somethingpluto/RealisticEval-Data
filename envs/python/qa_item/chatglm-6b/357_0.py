
def hill_sort(arr):
    """
    Sorts a list of integers using the Hill Sort (Shell Sort) algorithm.

    Args:
        arr (list of int): A list of integers that will be sorted in-place.
    """
    # Initialize the pivot element as the last element in the list
    pivot = arr[-1]
    # Iterate over the remaining elements of the list
    for i in range(len(arr) - 2):
        # If the current element is less than or equal to the pivot, swap it with the pivot
        if arr[i] <= pivot:
            arr[i], arr[pivot] = arr[pivot], arr[i]
        # If the current element is greater than the pivot, swap it with the next element
        else:
            arr[i], arr[pivot] = arr[pivot], arr[i]
    # Return the sorted list
    return arr

import unittest

def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
class Tester(unittest.TestCase):
    """
    Test cases for the hill_sort function.
    """
    
    def test_hill_sort_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        hill_sort(arr)
        self.assertTrue(is_sorted(arr))

    def test_hill_sort_reverse_order(self):
        arr = [5, 4, 3, 2, 1]
        hill_sort(arr)
        self.assertTrue(is_sorted(arr))

    def test_hill_sort_with_duplicates(self):
        arr = [3, 1, 2, 3, 2]
        hill_sort(arr)
        self.assertTrue(is_sorted(arr))

    def test_hill_sort_identical_values(self):
        arr = [1, 1, 1, 1, 1]
        hill_sort(arr)
        self.assertTrue(is_sorted(arr))

    def test_hill_sort_empty_array(self):
        arr = []
        hill_sort(arr)
        self.assertTrue(is_sorted(arr))

    def test_hill_sort_single_element(self):
        arr = [42]
        hill_sort(arr)
        self.assertTrue(is_sorted(arr))

    def test_hill_sort_large_random_array(self):
        arr = [3, 7, 2, 5, 1, 4, 6, 0, 9, 8]
        hill_sort(arr)
        self.assertTrue(is_sorted(arr))
if __name__ == '__main__':
    unittest.main()