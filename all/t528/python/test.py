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
