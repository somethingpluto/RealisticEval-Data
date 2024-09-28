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

    def test_none_and_nan(self):
        """ Test a dictionary with None and NaN values. """
        input_dict = {
            'key1': None,
            'key2': np.nan,
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
