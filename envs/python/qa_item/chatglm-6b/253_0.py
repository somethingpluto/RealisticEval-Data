
def log(item: any) -> any:
    if not isinstance(item, str):
        raise ValueError("Item must be a string")
    if not isinstance(item, int):
        raise ValueError("Item must be an integer")
    if not isinstance(item, list):
        raise ValueError("Item must be a list")
    if not isinstance(item, dict):
        raise ValueError("Item must be a dictionary")
    
    print(f"{item}: {item}")
    
    if isinstance(item, str):
        item = f"{item}: {item}"
    elif isinstance(item, int):
        item = f"{item}: {item}"
    elif isinstance(item, list):
        item = f"{item}: {item}"
    elif isinstance(item, dict):
        item = f"{item}: {item}"
    
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