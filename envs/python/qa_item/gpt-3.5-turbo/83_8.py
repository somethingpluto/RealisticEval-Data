from typing import List

def rotate_list_elements(elements: List[int]) -> List[int]:
    """
    Rotate the elements of the list to the left by one position. The first element
    is moved to the end of the list, and all other elements are shifted one position to the left.

    Args:
        elements (List[int]): A list of integers to be rotated.

    Returns:
        List[int]: The rotated list with elements shifted to the left by one position.
    """
    if len(elements) <= 1:
        return elements
    
    rotated_list = elements[1:]  # Extract all elements from index 1 to the end
    rotated_list.append(elements[0])  # Append the first element to the end
    
    return rotated_list
import unittest

class TestRotateListElements(unittest.TestCase):

    def test_basic_rotation(self):
        self.assertEqual(rotate_list_elements([1, 2, 3, 4]), [2, 3, 4, 1], "Should rotate the list elements correctly")

    def test_single_element_list(self):
        self.assertEqual(rotate_list_elements([10]), [10], "Single element list should remain unchanged")

    def test_empty_list(self):
        self.assertEqual(rotate_list_elements([]), [], "Empty list should remain unchanged")

    def test_two_element_list(self):
        self.assertEqual(rotate_list_elements([5, 9]), [9, 5], "Should correctly rotate a two-element list")

    def test_large_list(self):
        large_list = list(range(1, 1001))
        rotated_list = rotate_list_elements(large_list)
        self.assertEqual(rotated_list, list(range(2, 1001)) + [1], "Should correctly rotate a large list")




if __name__ == '__main__':
    unittest.main()