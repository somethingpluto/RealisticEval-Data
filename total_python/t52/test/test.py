import unittest
from unittest.mock import patch, MagicMock
import os


class TestRenameFiles(unittest.TestCase):

    @patch('os.walk')
    @patch('os.rename')
    def test_simple_rename(self, mock_rename, mock_walk):
        # Simulate os.walk
        mock_walk.return_value = [
            ('/path', ('subdir',), ('file:1.txt',)),
        ]
        # Invoke the rename_files function
        rename_files('/path')
        # Check if os.rename was called correctly
        mock_rename.assert_called_once_with('/path/file:1.txt', '/path/file-1.txt')

    @patch('os.walk')
    @patch('os.rename')
    def test_no_rename_needed(self, mock_rename, mock_walk):
        # No colon in filenames
        mock_walk.return_value = [
            ('/path', ('subdir',), ('file1.txt',)),
        ]
        rename_files('/path')
        # os.rename should not be called
        mock_rename.assert_not_called()

    @patch('os.walk')
    @patch('os.rename')
    def test_multiple_files(self, mock_rename, mock_walk):
        # Multiple files, some need renaming
        mock_walk.return_value = [
            ('/path', ('subdir',), ('file:1.txt', 'file2.txt', 'file:3.txt')),
        ]
        rename_files('/path')
        # Check correct calls to os.rename
        calls = [
            unittest.mock.call('/path/file:1.txt', '/path/file-1.txt'),
            unittest.mock.call('/path/file:3.txt', '/path/file-3.txt')
        ]
        mock_rename.assert_has_calls(calls, any_order=True)

    @patch('os.walk')
    @patch('os.rename')
    def test_rename_error(self, mock_rename, mock_walk):
        # Simulate an error during renaming
        mock_walk.return_value = [
            ('/path', ('subdir',), ('file:1.txt',)),
        ]
        mock_rename.side_effect = OSError("Permission denied")
        with self.assertLogs(level='ERROR') as log:
            rename_files('/path')
            # Check if error was logged
            self.assertIn('Permission denied', log.output[0])

    @patch('os.walk')
    @patch('os.rename')
    def test_nested_directories(self, mock_rename, mock_walk):
        # Files in nested directories
        mock_walk.return_value = [
            ('/path', ('subdir',), ('file:1.txt',)),
            ('/path/subdir', (), ('file:2.txt',))
        ]
        rename_files('/path')
        # Check correct calls to os.rename for nested directories
        calls = [
            unittest.mock.call('/path/file:1.txt', '/path/file-1.txt'),
            unittest.mock.call('/path/subdir/file:2.txt', '/path/subdir/file-2.txt')
        ]
        mock_rename.assert_has_calls(calls, any_order=True)
