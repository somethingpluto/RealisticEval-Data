import os
import shutil
import unittest
from tempfile import mkdtemp
from unittest.mock import patch, mock_open


class TestFindJsonFilesWithKeyword(unittest.TestCase):
    def setUp(self):
        # Set up a temporary directory
        self.test_dir = mkdtemp()
        self.test_file_path = os.path.join(self.test_dir, 'test.js.json')
        with open(self.test_file_path, 'w') as f:
            f.write('{"key": "value with keyword"}')

    def tearDown(self):
        # Remove the directory after test
        shutil.rmtree(self.test_dir)

    @patch('os.walk')
    @patch('builtins.open', new_callable=mock_open, read_data='{"key": "value with keyword"}')
    @patch('json.load', return_value={"key": "value with keyword"})
    def test_keyword_in_single_file(self, mock_json_load, mock_file, mock_os_walk):
        mock_os_walk.return_value = [
            (self.test_dir, (), ('test.js.json',)),
        ]
        expected = ['test.js.json']
        result = find_json_files_with_keyword(self.test_dir, 'keyword')
        self.assertEqual(result, expected)

    @patch('os.walk')
    @patch('builtins.open', new_callable=mock_open, read_data='{"key": "no keyword here"}')
    @patch('json.load', return_value={"key": "no keyword here"})
    def test_keyword_not_in_file(self, mock_json_load, mock_file, mock_os_walk):
        mock_os_walk.return_value = [
            (self.test_dir, (), ('test.js.json',)),
        ]
        expected = []
        result = find_json_files_with_keyword(self.test_dir, 'wc')
        self.assertEqual(result, expected)

    @patch('os.walk')
    def test_no_json_files_in_directory(self, mock_os_walk):
        # Use an empty temporary directory set up in setUp
        mock_os_walk.return_value = [
            (self.test_dir, (), ()),
        ]
        expected = []
        result = find_json_files_with_keyword(self.test_dir, 'keyword')
        self.assertEqual(result, expected)

    @patch('os.walk')
    @patch('builtins.open', new_callable=mock_open, read_data='{"key": "keyword present here"}')
    @patch('json.load', return_value={"key": "keyword present here"})
    def test_multiple_json_files(self, mock_json_load, mock_file, mock_os_walk):
        # Create multiple files in setUp
        file1_path = os.path.join(self.test_dir, 'file1.json')
        file2_path = os.path.join(self.test_dir, 'file2.json')
        with open(file1_path, 'w') as f:
            f.write('{"key": "keyword present here"}')
        with open(file2_path, 'w') as f:
            f.write('{"key": "keyword present here"}')
        mock_os_walk.return_value = [
            (self.test_dir, (), ('file1.json', 'file2.json')),
        ]
        expected = ['file1.json', 'file2.json']
        result = find_json_files_with_keyword(self.test_dir, 'keyword')
        self.assertEqual(result, expected)
