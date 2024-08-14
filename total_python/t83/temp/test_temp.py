import unittest


class TestRotateList(unittest.TestCase):
    def test_standard_list(self):
        # Test a standard list with multiple elements
        self.assertEqual(rotate_list([1, 2, 3, 4]), [2, 3, 4, 1])

    def test_single_element_list(self):
        # Test a list with only one element
        self.assertEqual(rotate_list([1]), [1])

    def test_empty_list(self):
        # Test an empty list
        self.assertEqual(rotate_list([]), [])

    def test_list_with_duplicates(self):
        # Test a list that contains duplicate values
        self.assertEqual(rotate_list([1, 2, 2, 3]), [2, 2, 3, 1])

    def test_list_with_varied_types(self):
        # Test a list containing elements of different types
        self.assertEqual(rotate_list(['a', 123, None, True]), [123, None, True, 'a'])

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
