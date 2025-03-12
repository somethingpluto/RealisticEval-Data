from typing import Dict
import re

def clean_dictionary(input_dict: Dict) -> Dict:
    """
    Cleans the input dictionary by removing keys with invalid values. Valid values are non-NaN, non-None, and non-whitespace strings.

    Args:
        input_dict (Dict): A dictionary to be cleaned.

    Returns:
        Dict: A new dictionary containing only valid values.
    """
    def is_valid_value(value):
        if value is None:
            return False
        if isinstance(value, str):
            return bool(re.search(r'\S', value))  # Check for non-whitespace characters
        return True

    return {key: value for key, value in input_dict.items() if is_valid_value(value)}
import unittest

import numpy as np


class TestCleanDictionary(unittest.TestCase):

    def test_valid_strings(self):
        """ Test a dictionary with valid strings. """
        input_dict = {
            'key1': 'valid string',
            'key2': 'another valid string'
        }
        expected_output = {
            'key1': 'valid string',
            'key2': 'another valid string'
        }
        self.assertEqual(clean_dictionary(input_dict), expected_output)

    def test_none_and(self):
        """ Test a dictionary with None and NaN values. """
        input_dict = {
            'key1': None,
            'key3': 'valid string'
        }
        expected_output = {
            'key3': 'valid string'
        }
        self.assertEqual(clean_dictionary(input_dict), expected_output)

    def test_whitespace_strings(self):
        """ Test a dictionary with whitespace strings. """
        input_dict = {
            'key1': '   ',
            'key2': '',
            'key3': 'valid'
        }
        expected_output = {
            'key3': 'valid'
        }
        self.assertEqual(clean_dictionary(input_dict), expected_output)

    def test_empty_dictionary(self):
        """ Test an empty dictionary. """
        input_dict = {}
        expected_output = {}
        self.assertEqual(clean_dictionary(input_dict), expected_output)

if __name__ == '__main__':
    unittest.main()