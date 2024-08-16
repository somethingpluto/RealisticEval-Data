import unittest
from unittest.mock import patch


class TestLogFunction(unittest.TestCase):
    @patch('builtins.print')
    def test_log_string(self, mock_print):
        """ Test logging a simple string """
        log("Hello, world!")
        mock_print.assert_called_once_with("Hello, world!")

    @patch('builtins.print')
    def test_log_number(self, mock_print):
        """ Test logging a number """
        log(123.456)
        mock_print.assert_called_once_with(123.456)

    @patch('builtins.print')
    def test_log_dictionary(self, mock_print):
        """ Test logging a dictionary as JSON """
        log({"key": "value", "number": 42})
        expected_json_output = '{\n    "key": "value",\n    "number": 42\n}'
        mock_print.assert_called_once_with(expected_json_output)

    @patch('builtins.print')
    def test_log_list(self, mock_print):
        """ Test logging a list as JSON """
        log([1, 2, 3, 4, 5])
        expected_json_output = '[\n    1,\n    2,\n    3,\n    4,\n    5\n]'
        mock_print.assert_called_once_with(expected_json_output)

    @patch('builtins.print')
    def test_log_unsupported_type(self, mock_print):
        """ Test logging an unsupported type """
        log(self)
        expected_error_message = f"Error: Unsupported type {type(self).__name__} for logging."
        mock_print.assert_called_once_with(expected_error_message)

import json

def log(item):
    """
    Logs an item by printing it. Handles strings, numbers, lists, and dictionaries by printing
    them directly or as a JSON-formatted string. Other types are reported as errors.

    Args:
    item: The item to be logged. Can be of any type.
    """
    # Handling for strings, integers, and floats
    if isinstance(item, (str, int, float)):
        print(item)
    # Handling for dictionaries and lists to convert to JSON string
    elif isinstance(item, (dict, list)):
        try:
            print(json.dumps(item, indent=4))  # Pretty print JSON for better readability
        except TypeError as e:
            print(f"Error: Failed to serialize item to JSON. {e}")
    else:
        # Print an informative error message for unsupported types
        print(f"Error: Unsupported type {type(item).__name__} for logging.")