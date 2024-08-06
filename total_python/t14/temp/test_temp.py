import unittest
from unittest.mock import patch, mock_open


class TestFindJsonFilesWithKeyword(unittest.TestCase):
    @patch('os.walk')
    @patch('builtins.open', new_callable=mock_open, read_data='{"key": "value with keyword"}')
    @patch('json.load', return_value={"key": "value with keyword"})
    def test_keyword_in_single_file(self, mock_json_load, mock_file, mock_os_walk):
        mock_os_walk.return_value = [
            ('/some/folder', (), ('test.json',)),
        ]
        expected = ['test.json']
        result = find_json_files_with_keyword('/some/folder', 'keyword')
        self.assertEqual(result, expected)

    @patch('os.walk')
    @patch('builtins.open', new_callable=mock_open, read_data='{"key": "no keyword here"}')
    @patch('json.load', return_value={"key": "no keyword here"})
    def test_keyword_not_in_file(self, mock_json_load, mock_file, mock_os_walk):
        mock_os_walk.return_value = [
            ('/some/folder', (), ('test.json',)),
        ]
        expected = []
        result = find_json_files_with_keyword('/some/folder', 'wc')
        self.assertEqual(result, expected)

    @patch('os.walk')
    def test_no_json_files_in_directory(self, mock_os_walk):
        mock_os_walk.return_value = [
            ('/some/folder', (), ('test.txt', 'image.png')),
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
import json
import os
from typing import List


def find_json_files_with_keyword(directory:str, keyword:str) ->List[str]:
    """
    Search all JSON files in the specified directory for a given keyword
    and return a list of filenames that contain the keyword.

    Args:
        directory (str): Path to the directory where JSON files are stored.
        keyword (str): Keyword to search for within the JSON files.

    Returns:
        list: A list of filenames (str) of JSON files containing the keyword.
    """
    matching_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    if keyword in json.dumps(data):
                        matching_files.append(file)
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
    return matching_files
