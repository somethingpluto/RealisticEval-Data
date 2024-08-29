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
    if len(elements) > 1:
        elements = elements[1:] + [elements[0]]
    return elements

def rotate_list(elements):
    """
    Rotate the elements of the list, moving the first element to the end and shifting all others forward.

    Args:
    elements (list): The list of elements to rotate.

    Returns:
    list: The list after rotation.
    """
    if not elements:
        return elements  # Return the list as is if it's empty

    # Move the first element to the last and shift others forward
    rotated_list = elements[1:] + elements[:1]

    return rotated_list

