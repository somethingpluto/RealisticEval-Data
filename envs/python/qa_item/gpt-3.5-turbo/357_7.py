from typing import List

def hill_sort(arr: List[int]):
    def gap_insertion_sort(arr, start, gap):
        for i in range(start + gap, len(arr), gap):
            current_val = arr[i]
            position = i

            while position >= gap and arr[position - gap] > current_val:
                arr[position] = arr[position - gap]
                position -= gap

            arr[position] = current_val

    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap):
            gap_insertion_sort(arr, i, gap)
        gap //= 2
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