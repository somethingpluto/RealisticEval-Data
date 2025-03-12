from typing import List

def binary_search_closest(array: List[int], target: int) -> int:
    """
    Performs a binary search to find the index of the target value in a sorted array.
    If the target value is not found, it returns the index of the closest value.

    Args:
        array (List[int]): The sorted array in which to search.
        target (int): The target value to search for.

    Returns:
        int: The index of the target or the index of the closest value if the target is not found.
    """
    left, right = 0, len(array) - 1
    closest_index = -1
    closest_distance = float('inf')

    while left <= right:
        mid = (left + right) // 2
        mid_value = array[mid]

        if mid_value == target:
            return mid

        # Update closest index if the current mid value is closer to the target
        if abs(mid_value - target) < closest_distance:
            closest_distance = abs(mid_value - target)
            closest_index = mid

        if mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return closest_index
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