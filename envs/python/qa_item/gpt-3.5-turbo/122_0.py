from typing import List

def safe_splice(input_array:List, amount_to_remove:int, index_to_remove:int, replace_with=None) -> List:
    """
    Safely splices an array by removing a specified number of elements from a given index,
    and optionally replaces them with a new element.

    Args:
        input_array (list): The original array to be modified.
        amount_to_remove (int): The number of elements to remove from the array.
        index_to_remove (int): The index at which to start removing elements.
        replace_with (any, optional): The element to replace the removed elements with.

    Returns:
        list: A new array with the specified elements removed and optionally replaced.
    """
    
    if index_to_remove < 0 or index_to_remove >= len(input_array):
        return input_array
    
    new_array = input_array.copy()
    
    del new_array[index_to_remove:index_to_remove+amount_to_remove]
    
    if replace_with is not None:
        new_array.insert(index_to_remove, replace_with)
        
    return new_array
import unittest


class TestSafeSplice(unittest.TestCase):

    def test_replaces_removed_elements_with_a_new_element(self):
        input_array = ['a', 'b', 'c', 'd', 'e']
        expected = ['a', 'z', 'e']
        result = safe_splice(input_array, 3, 1, 'z')
        self.assertEqual(result, expected)

    def test_removes_specified_elements_and_replaces_with_new_element(self):
        input_array = [1, 2, 3, 4, 5]
        amount_to_remove = 2
        index_to_remove = 1
        replace_with = 99
        result = safe_splice(input_array, amount_to_remove, index_to_remove, replace_with)
        self.assertEqual(result, [1, 99, 4, 5])

    def test_handles_removing_elements_from_the_end_of_the_array(self):
        input_array = [1, 2, 3, 4, 5]
        amount_to_remove = 2
        index_to_remove = 3
        result = safe_splice(input_array, amount_to_remove, index_to_remove)
        self.assertEqual(result, [1, 2, 3])

    def test_handles_case_where_no_elements_are_removed(self):
        input_array = [1, 2, 3, 4, 5]
        amount_to_remove = 0
        index_to_remove = 2
        replace_with = 99
        result = safe_splice(input_array, amount_to_remove, index_to_remove, replace_with)
        self.assertEqual(result, [1, 2, 99, 3, 4, 5])

    def test_handles_edge_case_with_empty_input_array(self):
        input_array = []
        amount_to_remove = 1
        index_to_remove = 0
        replace_with = 99
        result = safe_splice(input_array, amount_to_remove, index_to_remove, replace_with)
        self.assertEqual(result, [99])

if __name__ == '__main__':
    unittest.main()