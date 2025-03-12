from typing import List

def bubble_sort(arr: List[int]):
    n = len(arr)
    for i in range(n):
        # Flag to check if any swapping is done in the current iteration
        swapped = False
        
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # If no swapping is done, the array is already sorted
        if not swapped:
            break
import unittest


class Tester(unittest.TestCase):

    def test_sorted_array(self):
        """Test Case 1: Sorting an already sorted array"""
        arr1 = [1, 2, 3, 4, 5]
        bubble_sort(arr1)
        self.assertEqual(arr1, [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        """Test Case 2: Sorting a reverse sorted array"""
        arr2 = [5, 4, 3, 2, 1]
        bubble_sort(arr2)
        self.assertEqual(arr2, [1, 2, 3, 4, 5])

    def test_array_with_duplicates(self):
        """Test Case 3: Sorting an array with duplicate elements"""
        arr3 = [3, 1, 2, 3, 2]
        bubble_sort(arr3)
        self.assertEqual(arr3, [1, 2, 2, 3, 3])

    def test_single_element_array(self):
        """Test Case 4: Sorting an array with a single element"""
        arr4 = [1]
        bubble_sort(arr4)
        self.assertEqual(arr4, [1])

    def test_empty_array(self):
        """Test Case 5: Sorting an empty array"""
        arr5 = []
        bubble_sort(arr5)
        self.assertEqual(arr5, [])

if __name__ == '__main__':
    unittest.main()