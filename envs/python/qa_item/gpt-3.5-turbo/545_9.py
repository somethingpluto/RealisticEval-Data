from typing import List, Any

def elements_before_null(array: List[Any]) -> List[Any]:
    """
    Iterates through the array of elements until the first None is encountered,
    returning a new list that includes all elements before None.

    Args:
        array (List[Any]): The array to iterate through.

    Returns:
        List[Any]: A new list containing elements before the first None.
    """  

    result = []
    for item in array:
        if item is None:
            break
        result.append(item)
    
    return result
import unittest


class TestElementsBeforeNull(unittest.TestCase):

    def test_returns_elements_before_first_null(self):
        input_array = ['element1', 'element2', None, 'element3', 'element4']
        result = elements_before_null(input_array)
        self.assertEqual(result, ['element1', 'element2'])

    def test_returns_empty_array_when_input_is_empty(self):
        input_array = []
        result = elements_before_null(input_array)
        self.assertEqual(result, [])

    def test_returns_same_array_if_no_null(self):
        input_array = ['element1', 'element2', 'element3']
        result = elements_before_null(input_array)
        self.assertEqual(result, ['element1', 'element2', 'element3'])

    def test_returns_empty_array_if_first_element_is_null(self):
        input_array = [None, 'element2', 'element3']
        result = elements_before_null(input_array)
        self.assertEqual(result, [])

    def test_handles_mixed_types_with_null(self):
        input_array = [1, 'text', None, True, False]
        result = elements_before_null(input_array)
        self.assertEqual(result, [1, 'text'])

    def test_handles_array_with_only_null(self):
        input_array = [None]
        result = elements_before_null(input_array)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()