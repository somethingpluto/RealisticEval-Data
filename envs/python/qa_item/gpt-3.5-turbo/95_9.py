from typing import List, Any, Callable, Dict


def find_matching_elements(arr: List[Any], comparison_fn: Callable[[Any], bool]) -> List[Dict[str, Any]]:
    """
    Finds matching elements and their indices in the input array
    based on the specified comparison function.
    Args:
        arr (str): The input array to search through.
        comparison_fn (): The comparison function to determine matches.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries, each containing the matched element and its index.
    """
import unittest


class TestFindMatchingElements(unittest.TestCase):

    def test_empty_input_array(self):
        result = find_matching_elements([], lambda el: el > 0)
        self.assertEqual(result, [])

    def test_matching_elements_and_indices(self):
        input_array = [1, 2, 3, 4, 5]
        comparison_function = lambda num: num > 3
        result = find_matching_elements(input_array, comparison_function)
        self.assertEqual(result, [
            {'element': 4, 'index': 3},
            {'element': 5, 'index': 4},
        ])

    def test_string_matching_condition(self):
        input_array = ['apple', 'banana', 'cherry', 'date']
        comparison_function = lambda fruit: fruit.startswith('b')
        result = find_matching_elements(input_array, comparison_function)
        self.assertEqual(result, [
            {'element': 'banana', 'index': 1},
        ])

    def test_multiple_elements_with_same_value(self):
        input_array = [1, 2, 2, 3, 2, 4]
        comparison_function = lambda num: num == 2
        result = find_matching_elements(input_array, comparison_function)
        self.assertEqual(result, [
            {'element': 2, 'index': 1},
            {'element': 2, 'index': 2},
            {'element': 2, 'index': 4},
        ])

    def test_matching_objects_based_on_property(self):
        input_array = [
            {'name': 'Alice', 'age': 25},
            {'name': 'Bob', 'age': 30},
            {'name': 'Charlie', 'age': 30},
        ]
        comparison_function = lambda person: person['age'] == 30
        result = find_matching_elements(input_array, comparison_function)
        self.assertEqual(result, [
            {'element': {'name': 'Bob', 'age': 30}, 'index': 1},
            {'element': {'name': 'Charlie', 'age': 30}, 'index': 2},
        ])

    def test_no_elements_if_no_matches_found(self):
        input_array = [1, 3, 5, 7]
        comparison_function = lambda num: num % 2 == 0  # looking for even numbers
        result = find_matching_elements(input_array, comparison_function)
        self.assertEqual(result, [])

    def test_negative_numbers_condition(self):
        input_array = [-1, -2, 0, 1, 2]
        comparison_function = lambda num: num < 0
        result = find_matching_elements(input_array, comparison_function)
        self.assertEqual(result, [
            {'element': -1, 'index': 0},
            {'element': -2, 'index': 1},
        ])

if __name__ == '__main__':
    unittest.main()