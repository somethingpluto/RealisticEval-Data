import unittest
from unittest.mock import patch, mock_open


class TestFindJsonFilesWithKeyword(unittest.TestCase):
    @patch('os.walk')
    @patch('builtins.open', new_callable=mock_open, read_data='{"key": "value with keyword"}')
    @patch('json.load', return_value={"key": "value with keyword"})
    def test_keyword_in_single_file(self, mock_json_load, mock_file, mock_os_walk):
        mock_os_walk.return_value = [
            ('/some/folder', (), ('test.js.json',)),
        ]
        expected = ['test.js.json']
        result = find_json_files_with_keyword('/some/folder', 'keyword')
        self.assertEqual(result, expected)

    @patch('os.walk')
    @patch('builtins.open', new_callable=mock_open, read_data='{"key": "no keyword here"}')
    @patch('json.load', return_value={"key": "no keyword here"})
    def test_keyword_not_in_file(self, mock_json_load, mock_file, mock_os_walk):
        mock_os_walk.return_value = [
            ('/some/folder', (), ('test.js.json',)),
        ]
        expected = []
        result = find_json_files_with_keyword('/some/folder', 'wc')
        self.assertEqual(result, expected)

    @patch('os.walk')
    def test_no_json_files_in_directory(self, mock_os_walk):
        mock_os_walk.return_value = [
            ('/some/folder', (), ('test.js.txt', 'image.png')),
        ]
        expected = []
        result = find_json_files_with_keyword('/some/folder', 'keyword')
        self.assertEqual(result, expected)

    @patch('os.walk')
    @patch('builtins.open', new_callable=mock_open, read_data='{"key": "keyword present here"}')
    @patch('json.load', return_value={"key": "keyword present here"})
    def test_multiple_json_files(self, mock_json_load, mock_file, mock_os_walk):
        mock_os_walk.return_value = [
            ('/some/folder', (), ('file1.json', 'file2.json')),
        ]
        expected = ['file1.json', 'file2.json']
        result = find_json_files_with_keyword('/some/folder', 'keyword')
        self.assertEqual(result, expected)

    @patch('os.walk')
    @patch('builtins.open', new_callable=mock_open, read_data='{"key": "error expected"}')
    @patch('json.load', side_effect=Exception("Failed to load JSON"))
    def test_json_parsing_error(self, mock_json_load, mock_file, mock_os_walk):
        mock_os_walk.return_value = [
            ('/some/folder', (), ('corrupt.json',)),
        ]
        expected = []  # Assuming the function does not crash and handles errors gracefully
        result = find_json_files_with_keyword('/some/folder', 'keyword')
        self.assertEqual(result, expected)
