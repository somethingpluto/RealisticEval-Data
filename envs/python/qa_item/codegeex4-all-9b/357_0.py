def hill_sort(arr: list):
    """
    Sorts a list of integers using the Hill Sort (Shell Sort) algorithm.

    Args:
        arr (list of int): A list of integers that will be sorted in-place.
    """
    def gap_insertion_sort(arr, start, gap):
        for i in range(start + gap, len(arr), gap):
            key = arr[i]
            j = i - gap
            while j >= start and arr[j] > key:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = key

    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            gap_insertion_sort(arr, 0, gap)
        gap //= 2

    return arr
import unittest

from more_itertools import is_sorted


class Tester(unittest.TestCase):
    def test_hill_sort(self):
        # Test case: Sort an already sorted array
        arr = [1, 2, 3, 4, 5]
        hill_sort(arr)
        self.assertTrue(is_sorted(arr))

        # Test case: Sort an array in reverse order
        arr = [5, 4, 3, 2, 1]
        hill_sort(arr)
        self.assertTrue(is_sorted(arr))

        # Test case: Sort an array with duplicate values
        arr = [3, 1, 2, 3, 2]
        hill_sort(arr)
        self.assertTrue(is_sorted(arr))

        # Test case: Sort an array with all identical values
        arr = [1, 1, 1, 1, 1]
        hill_sort(arr)
        self.assertTrue(is_sorted(arr))

        # Test case: Sort an empty array
        arr = []
        hill_sort(arr)
        self.assertTrue(is_sorted(arr))

        # Test case: Sort an array with one element
        arr = [42]
        hill_sort(arr)
        self.assertTrue(is_sorted(arr))

        # Test case: Sort a large random array
        arr = [3, 7, 2, 5, 1, 4, 6, 0, 9, 8]
        hill_sort(arr)
        self.assertTrue(is_sorted(arr))

if __name__ == '__main__':
    unittest.main()