from typing import List, Dict, Union


def convert_strings_to_numbers(data: Union[Dict, List]) -> Union[Dict, List]:
    """
    Convert strings in nested structures (e.g. dictionaries, arrays) to numbers (integers or floating point numbers) as much as possible

    Args:
        data (Union[Dict,List]): before convert data

    Returns:
        Union[Dict,List]: after convert data
    """
    if isinstance(data, dict):
        return {key: convert_strings_to_numbers(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [convert_strings_to_numbers(item) for item in data]
    elif isinstance(data, str):
        try:
            return int(data) if data.isdigit() else float(data)
        except ValueError:
            return data
    else:
        return data
import unittest


class TestConvertStringsToNumbers(unittest.TestCase):

    def test_flat_dict(self):
        data = {'a': '1', 'b': '2.5', 'c': 'not a number'}
        expected = {'a': 1, 'b': 2.5, 'c': 'not a number'}
        self.assertEqual(convert_strings_to_numbers(data), expected)

    def test_nested_dict(self):
        data = {'x': {'y': '10', 'z': '3.14'}, 'w': '20.0'}
        expected = {'x': {'y': 10, 'z': 3.14}, 'w': 20.0}
        self.assertEqual(convert_strings_to_numbers(data), expected)

    def test_list_of_strings(self):
        data = ['1', '2.5', '3', 'invalid']
        expected = [1, 2.5, 3, 'invalid']
        self.assertEqual(convert_strings_to_numbers(data), expected)

    def test_mixed_structure(self):
        data = {'numbers': ['1', '2.0', 3], 'more_numbers': [{'num': '4'}, '5']}
        expected = {'numbers': [1, 2.0, 3], 'more_numbers': [{'num': 4}, 5]}
        self.assertEqual(convert_strings_to_numbers(data), expected)

    def test_empty_structure(self):
        data = {}
        expected = {}
        self.assertEqual(convert_strings_to_numbers(data), expected)
if __name__ == '__main__':
    unittest.main()