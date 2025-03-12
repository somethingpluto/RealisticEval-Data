import re
from typing import List, Dict, Union

def convert_strings_to_numbers(data: Union[Dict, List]) -> Union[Dict, List]:
    if isinstance(data, list):
        return [convert_strings_to_numbers(item) for item in data]
    elif isinstance(data, dict):
        return {key: convert_strings_to_numbers(value) for key, value in data.items()}
    elif isinstance(data, str) and data.isdigit():
        return float(data)
    else:
        return data

    # Additional check to handle non-numeric strings
    for key, value in data.items():
        if isinstance(value, str) and not value.isdigit() and re.match(r'^-?\d+(\.\d+)?$', value) is None:
            data[key] = value
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