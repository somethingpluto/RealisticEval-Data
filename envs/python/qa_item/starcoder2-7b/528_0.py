import os

def find_markdown_files(dir_path: str) -> list:
    """
    Searches for Markdown files in the specified directory and returns the paths of the files as a list.

    Args:
        dir_path (str): The directory path to search in.

    Returns:
        list: A list of paths to Markdown files.
    """
    markdown_files = [f for f in os.listdir(dir_path) if f.endswith('.md') or f.endswith('.markdown')]
    return markdown_files
import unittest
from unittest.mock import patch


class TestFindMarkdownFiles(unittest.TestCase):

    @patch('os.listdir')
    @patch('os.path.isdir')
    def test_empty_directory(self, mock_isdir, mock_listdir):
        mock_listdir.return_value = []
        mock_isdir.return_value = False

        result = find_markdown_files('emptyDir')
        self.assertEqual(result, [])

    @patch('os.listdir')
    @patch('os.path.isdir')
    def test_one_markdown_file(self, mock_isdir, mock_listdir):
        mock_listdir.return_value = ['file1.md']
        mock_isdir.return_value = False

        result = find_markdown_files('dir')
        self.assertEqual(result, ['dir/file1.md'])

    @patch('os.listdir')
    @patch('os.path.isdir')
    def test_multiple_markdown_files(self, mock_isdir, mock_listdir):
        mock_listdir.return_value = ['file1.md', 'file2.md']
        mock_isdir.return_value = False

        result = find_markdown_files('dir')
        self.assertEqual(result, ['dir/file1.md', 'dir/file2.md'])

    @patch('os.listdir')
    @patch('os.path.isdir')
    def test_ignore_non_markdown_files(self, mock_isdir, mock_listdir):
        mock_listdir.return_value = ['file1.txt', 'file2.md', 'file3.doc']
        mock_isdir.return_value = False

        result = find_markdown_files('dir')
        self.assertEqual(result, ['dir/file2.md'])

    @patch('os.listdir')
    @patch('os.path.isdir')
    def test_only_non_markdown_files(self, mock_isdir, mock_listdir):
        mock_listdir.return_value = ['file1.txt', 'file2.doc']
        mock_isdir.return_value = False

        result = find_markdown_files('dir')
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()