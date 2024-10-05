import os
import unittest
from unittest.mock import patch, mock_open


class TestReadTxtAddJsonBracket(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='{"key": "value"}')
    def test_valid_json(self, mock_file):
        result = read_txt_add_json_bracket("fakefile.txt")
        self.assertEqual(result, [{"key": "value"}])


    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_file_not_found(self, mock_file):
        result = read_txt_add_json_bracket("non_existent_file.txt")
        self.assertEqual(result, [])

    @patch("builtins.open", new_callable=mock_open, read_data='{"key": value}')  # Invalid JSON
    def test_invalid_json(self, mock_file):
        result = read_txt_add_json_bracket("fakefile.txt")
        self.assertEqual(result, [])


    @patch("builtins.open", new_callable=mock_open, read_data='[]')
    def test_empty_json_array(self, mock_file):
        result = read_txt_add_json_bracket("fakefile.txt")
        self.assertEqual(result, [[]])  # Should return an empty list

    @patch("builtins.open", new_callable=mock_open, read_data='{"key": "value"  "key2": "value2"}')  # Missing comma
    def test_invalid_json_missing_comma(self, mock_file):
        result = read_txt_add_json_bracket("fakefile.txt")
        self.assertEqual(result, [])
