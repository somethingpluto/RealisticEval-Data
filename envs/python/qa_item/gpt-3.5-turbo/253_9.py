import json

def log(item: any) -> any:
    """
    Logs an item by printing it. Handles strings, numbers, lists, and dictionaries by printing
    them directly or as a JSON-formatted string. Other types are reported as errors.
    Args:
        item (any): The item to be logged. Can be of any type.

    Returns:
        item: The item to be logged. Can be of any type.
    """
    if isinstance(item, str) or isinstance(item, int) or isinstance(item, float):
        print(item)
    elif isinstance(item, list) or isinstance(item, dict):
        print(json.dumps(item))
    else:
        print("Error: Unsupported type for logging")
    return item
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
if __name__ == '__main__':
    unittest.main()