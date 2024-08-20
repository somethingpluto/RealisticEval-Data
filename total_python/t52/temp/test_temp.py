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

import os

def rename_files(directory_path):
    """
    Recursively renames files within a given directory by replacing colons in filenames with dashes.

    Parameters:
    - directory_path (str): The path to the directory where files will be renamed.

    Returns:
    - None
    """
    # Walk through all subdirectories of the provided directory
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            # Construct the full path of the current file
            old_file_path = os.path.join(root, file)
            # Replace colons with dashes in the filename
            new_file_name = file.replace(':', '-')
            new_file_path = os.path.join(root, new_file_name)

            # Only attempt to rename if the new name is different from the old name
            if old_file_path != new_file_path:
                try:
                    # Perform the file rename
                    os.rename(old_file_path, new_file_path)
                    print(f"Renamed '{old_file_path}' to '{new_file_path}'")
                except OSError as error:
                    # Handle potential errors during the rename operation, e.g., file being used by another process
                    print(f"Error renaming '{old_file_path}' to '{new_file_path}': {error}")