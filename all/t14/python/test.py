import json
import os
import unittest
from unittest.mock import patch, mock_open


class TestFindJsonFilesWithKeyword(unittest.TestCase):
    def setUp(self):
        # Setup code to create directory and files if needed
        self.test_dir = '/testdir'
        os.makedirs(self.test_dir, exist_ok=True)
        # Example of creating files, this is typically mocked in actual tests
        with open(os.path.join(self.test_dir, 'test.json'), 'w') as f:
            json.dump({"key": "value"}, f)
        with open(os.path.join(self.test_dir, 'file1.json'), 'w') as f:
            json.dump({"key": "value"}, f)
        with open(os.path.join(self.test_dir, 'file2.json'), 'w') as f:
            json.dump({"key": "value"}, f)

    def tearDown(self):
        # Teardown code to remove directories and files
        for root, dirs, files in os.walk(self.test_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.test_dir)

    @patch('os.walk')
    @patch('builtins.open', new_callable=mock_open, read_data='{"key": "value"}')
    def test_single_file_match(self, mock_file, mock_walk):
        mock_walk.return_value = [(self.test_dir, (None,), ('test.json',))]
        result = find_json_files_with_keyword(self.test_dir, 'value')
        self.assertEqual(result, ['test.json'])

    @patch('os.walk')
    @patch('builtins.open', mock_open(read_data='{"key": "value"}'))
    def test_multiple_files_match(self, mock_walk):
        mock_walk.return_value = [(self.test_dir, (None,), ('file1.json', 'file2.json'))]
        result = find_json_files_with_keyword(self.test_dir, 'value')
        self.assertEqual(result, ['file1.json', 'file2.json'])

    @patch('os.walk')
    def test_no_json_files(self, mock_walk):
        mock_walk.return_value = [(self.test_dir, (None,), ('file1.txt', 'file2.doc'))]
        result = find_json_files_with_keyword(self.test_dir, 'value')
        self.assertEqual(result, [])

    @patch('os.walk')
    @patch('builtins.open', new_callable=mock_open, read_data='{"key": ["nested_value"]}')
    def test_nested_keyword_match(self, mock_file, mock_walk):
        mock_walk.return_value = [(self.test_dir, (None,), ('test.json',))]
        result = find_json_files_with_keyword(self.test_dir, 'nested_value')
        self.assertEqual(result, ['test.json'])

    @patch('os.walk')
    @patch('builtins.open', mock_open(read_data='{}'))
    def test_empty_json_file(self, mock_walk):
        mock_walk.return_value = [(self.test_dir, (None,), ('empty.json',))]
        result = find_json_files_with_keyword(self.test_dir, 'value')
        self.assertEqual(result, [])

    @patch('os.walk')
    @patch('builtins.open', side_effect=IOError("Failed to open"))
    def test_io_error_while_reading_file(self, mock_file, mock_walk):
        mock_walk.return_value = [(self.test_dir, (None,), ('corrupt.json',))]
        result = find_json_files_with_keyword(self.test_dir, 'value')
        self.assertEqual(result, [])  # or assert an error message if your function logs it