import unittest
from unittest.mock import patch


class TestRenameFiles(unittest.TestCase):

    @patch('os.walk')
    @patch('os.rename')
    def test_no_files_present(self, mock_rename, mock_walk):
        mock_walk.return_value = [('/some/path', (), ())]
        rename_files('/some/path')
        mock_rename.assert_not_called()

    @patch('os.walk')
    @patch('os.rename')
    def test_basic_renaming(self, mock_rename, mock_walk):
        mock_walk.return_value = [('/some/path', (), ('file:1.txt',))]
        rename_files('/some/path')
        mock_rename.assert_called_once_with('/some/path/file:1.txt', '/some/path\\file-1.txt')

    @patch('os.walk')
    @patch('os.rename')
    def test_no_colon_in_filenames(self, mock_rename, mock_walk):
        mock_walk.return_value = [('/some/path', (), ('file1.txt',))]
        rename_files('/some/path')
        mock_rename.assert_not_called()

    @patch('os.walk')
    @patch('os.rename')
    def test_nested_directories(self, mock_rename, mock_walk):
        mock_walk.return_value = [
            ('/some/path', ('subdir',), ('file:1.txt',)),
            ('/some/path/subdir', (), ('file:2.txt',))
        ]
        rename_files('/some/path')
        expected_calls = [
            unittest.mock.call('/some/path/file:1.txt', '/some/path/file-1.txt'),
            unittest.mock.call('/some/path/subdir/file:2.txt', '/some/path/subdir/file-2.txt')
        ]
        mock_rename.assert_has_calls(expected_calls, any_order=True)

    @patch('os.walk')
    @patch('os.rename')
    def test_rename_failure(self, mock_rename, mock_walk):
        mock_walk.return_value = [('/some/path', (), ('file:1.txt',))]
        mock_rename.side_effect = OSError('Permission denied')
        with self.assertLogs(level='ERROR') as log:
            rename_files('/some/path')
            self.assertIn('Error renaming', log.output[0])
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