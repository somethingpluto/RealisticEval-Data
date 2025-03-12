from typing import List, Callable

def filter_array(unfiltered_array: List, is_qualified: Callable) -> List:
    filtered_array = [element for element in unfiltered_array if is_qualified(element)]
    return filtered_array
import unittest


class TestFilterArray(unittest.TestCase):

    def test_filters_out_numbers_less_than_or_equal_to_ten(self):
        unfiltered_array = [5, 12, 3, 18, 7, 10, 15]
        result = filter_array(unfiltered_array, lambda x: x > 10)
        self.assertEqual(result, [12, 18, 15])

    def test_returns_empty_array_when_all_elements_are_disqualified(self):
        unfiltered_array = [1, 2, 3, 4, 5]
        result = filter_array(unfiltered_array, lambda x: x > 10)
        self.assertEqual(result, [])

    def test_returns_same_array_when_all_elements_are_qualified(self):
        unfiltered_array = [11, 12, 15, 20]
        result = filter_array(unfiltered_array, lambda x: x > 10)
        self.assertEqual(result, [11, 12, 15, 20])

    def test_handles_empty_array_input(self):
        unfiltered_array = []
        result = filter_array(unfiltered_array, lambda x: x > 10)
        self.assertEqual(result, [])

    def test_filters_out_strings_based_on_length(self):
        unfiltered_array = ['a', 'ab', 'abc', 'abcd', 'abcde']
        result = filter_array(unfiltered_array, lambda x: len(x)>3)
        self.assertEqual(result, ['abcd', 'abcde'])

    def test_correctly_filters_array_with_mixed_types(self):
        unfiltered_array = [1, 'hello', True, 'world', None]
        result = filter_array(unfiltered_array, lambda x: isinstance(x, str))
        self.assertEqual(result, ['hello', 'world'])

    def test_filters_based_on_object_property(self):
        unfiltered_array = [{'value': 3}, {'value': 5}, {'value': 7}]
        result = filter_array(unfiltered_array, lambda x: x > 5)
        self.assertEqual(result, [{'value': 7}])

    def test_returns_empty_array_when_no_qualifying_function_provided(self):
        unfiltered_array = [1, 2, 3, 4, 5]
        result = filter_array(unfiltered_array, lambda x: False)  # Always returns false
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()