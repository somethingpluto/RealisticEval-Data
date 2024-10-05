import unittest
from unittest.mock import patch, mock_open
import json
import os


class TestFindJsonFilesWithKeyword(unittest.TestCase):
    @patch('os.walk')
    @patch('builtins.open', new_callable=mock_open, read_data='{"key": "value"}')
    def test_single_file_match(self, mock_file, mock_walk):
        mock_walk.return_value = [
            ('/testdir', (None,), ('test.json',))
        ]
        result = find_json_files_with_keyword('/testdir', 'value')
        self.assertEqual(result, ['test.json'])

    @patch('os.walk')
    @patch('builtins.open', mock_open(read_data='{"key": "value"}'))
    def test_multiple_files_match(self, mock_walk):
        mock_walk.return_value = [
            ('/testdir', (None,), ('file1.json', 'file2.json'))
        ]
        result = find_json_files_with_keyword('/testdir', 'value')
        self.assertEqual(result, ['file1.json', 'file2.json'])

    @patch('os.walk')
    def test_no_json_files(self, mock_walk):
        mock_walk.return_value = [
            ('/testdir', (None,), ('file1.txt', 'file2.doc'))
        ]
        result = find_json_files_with_keyword('/testdir', 'value')
        self.assertEqual(result, [])

    @patch('os.walk')
    @patch('builtins.open', new_callable=mock_open, read_data='{"key": ["nested_value"]}')
    def test_nested_keyword_match(self, mock_file, mock_walk):
        mock_walk.return_value = [
            ('/testdir', (None,), ('test.json',))
        ]
        result = find_json_files_with_keyword('/testdir', 'nested_value')
        self.assertEqual(result, ['test.json'])

    @patch('os.walk')
    @patch('builtins.open', mock_open(read_data='{}'))
    def test_empty_json_file(self, mock_walk):
        mock_walk.return_value = [
            ('/testdir', (None,), ('empty.json',))
        ]
        result = find_json_files_with_keyword('/testdir', 'value')
        self.assertEqual(result, [])

    @patch('os.walk')
    @patch('builtins.open', side_effect=IOError("Failed to open"))
    def test_io_error_while_reading_file(self, mock_file, mock_walk):
        mock_walk.return_value = [
            ('/testdir', (None,), ('corrupt.json',))
        ]
        result = find_json_files_with_keyword('/testdir', 'value')
        self.assertEqual(result, [])  # or assert an error message if your function logs it
