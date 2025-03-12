from typing import List

def remove_element_in_array(array: List, element):
    """
    Removes the first occurrence of a specified element from a list.

    Args:
        array (list): The list from which to remove the element.
        element: The element to remove from the list.

    Returns:
        list: A new list with the element removed, or the original list if the element is not found.
    """
    if element in array:
        new_array = list(array)
        new_array.remove(element)
        return new_array
    else:
        return array
import unittest


class TestRemoveElementInArray(unittest.TestCase):

    def test_returns_original_array_when_element_not_found(self):
        result = remove_element_in_array([1, 2, 3, 4], 5)
        self.assertEqual(result, [1, 2, 3, 4])

    def test_handles_empty_array_correctly(self):
        result = remove_element_in_array([], 1)
        self.assertEqual(result, [])

    def test_removes_element_from_array_of_objects(self):
        obj1 = {'id': 1}
        obj2 = {'id': 2}
        obj3 = {'id': 3}
        result = remove_element_in_array([obj1, obj2, obj3], obj2)
        self.assertEqual(result, [obj1, obj3])

    def test_does_not_modify_original_array(self):
        original_array = [1, 2, 3]
        result = remove_element_in_array(original_array, 2)
        self.assertEqual(original_array, [1, 2, 3])
        self.assertEqual(result, [1, 3])

if __name__ == '__main__':
    unittest.main()