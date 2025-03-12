from typing import List

def binary_search_closest(array: List[int], target: int) -> int:
    low = 0
    high = len(array) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    if high < 0:
        return low
    if low >= len(array):
        return high
    
    if abs(array[low] - target) < abs(array[high] - target):
        return low
    else:
        return high
import unittest


class TestBinarySearchClosest(unittest.TestCase):

    def test_target_present(self):
        """Test when the target is present in the array."""
        array = [1, 3, 5, 7, 9, 11]
        target = 7
        result = binary_search_closest(array, target)
        self.assertEqual(result, 3, "Target should be found at index 3.")

    def test_closest_element_smaller(self):
        """Test when the target is not present and the closest element is smaller."""
        array = [1, 3, 5, 7, 9, 11]
        target = 6
        result = binary_search_closest(array, target)
        self.assertEqual(result, 2, "Closest element should be 5 at index 2.")

    def test_closest_element_larger(self):
        """Test when the target is not present and the closest element is larger."""
        array = [1, 3, 5, 7, 9, 11]
        target = 8
        result = binary_search_closest(array, target)
        self.assertEqual(result, 3, "Closest element should be 7 at index 3.")

    def test_target_smaller_than_all(self):
        """Test when the target is smaller than all elements in the array."""
        array = [1, 3, 5, 7, 9, 11]
        target = 0
        result = binary_search_closest(array, target)
        self.assertEqual(result, 0, "Closest element should be 1 at index 0.")

    def test_target_larger_than_all(self):
        """Test when the target is larger than all elements in the array."""
        array = [1, 3, 5, 7, 9, 11]
        target = 12
        result = binary_search_closest(array, target)
        self.assertEqual(result, 5, "Closest element should be 11 at index 5.")

if __name__ == '__main__':
    unittest.main()