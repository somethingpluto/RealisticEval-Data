import unittest
from unittest.mock import patch


class TestRenameFiles(unittest.TestCase):

    @patch('os.listdir')
    @patch('os.rename')
    def test_empty_directory(self, mock_rename, mock_listdir):
        mock_listdir.return_value = []
        rename_files('dummy_directory')
        mock_rename.assert_not_called()

    @patch('os.listdir')
    @patch('os.rename')
    def test_single_file(self, mock_rename, mock_listdir):
        mock_listdir.return_value = ['image001.png']
        with patch('builtins.print') as mock_print:
            rename_files('dummy_directory')
            mock_rename.assert_called_once_with('dummy_directory/image001.png', 'dummy_directory/image001.png')
            mock_print.assert_called_with("Renaming image001.png to image001.png")

    @patch('os.listdir')
    @patch('os.rename')
    def test_multiple_files_same_base(self, mock_rename, mock_listdir):
        mock_listdir.return_value = ['test001.png', 'test002.png']
        with patch('builtins.print') as mock_print:
            rename_files('dummy_directory')
            expected_calls = [
                unittest.mock.call('dummy_directory/test001.png', 'dummy_directory/test001.png'),
                unittest.mock.call('dummy_directory/test002.png', 'dummy_directory/test002.png')
            ]
            mock_rename.assert_has_calls(expected_calls, any_order=True)

    @patch('os.listdir')
    @patch('os.rename')
    def test_multiple_files_different_bases(self, mock_rename, mock_listdir):
        mock_listdir.return_value = ['apple001.png', 'banana001.png']
        with patch('builtins.print') as mock_print:
            rename_files('dummy_directory')
            expected_calls = [
                unittest.mock.call('dummy_directory/apple001.png', 'dummy_directory/apple001.png'),
                unittest.mock.call('dummy_directory/banana001.png', 'dummy_directory/banana001.png')
            ]
            mock_rename.assert_has_calls(expected_calls, any_order=True)

    @patch('os.listdir')
    @patch('os.rename')
    def test_complex_naming(self, mock_rename, mock_listdir):
        mock_listdir.return_value = ['image999-1.png', 'image999.png', 'image999-2.png']
        with patch('builtins.print') as mock_print:
            rename_files('dummy_directory')
            expected_calls = [
                unittest.mock.call('dummy_directory/image999-1.png', 'dummy_directory/image9991.png'),
                unittest.mock.call('dummy_directory/image999.png', 'dummy_directory/image9992.png'),
                unittest.mock.call('dummy_directory/image999-2.png', 'dummy_directory/image9993.png')
            ]
            mock_rename.assert_has_calls(expected_calls, any_order=True)

import os
import re


def rename_files(directory):
    # Helper function to extract the base name without trailing digits and optional hyphen
    def get_base_name(filename):
        return re.sub(r'(\d{3})(-\d)?(?=\.png$)', '', filename)

    # Get list of PNG files in the directory, ensuring case insensitivity
    png_files = [f for f in os.listdir(directory) if f.lower().endswith('.png')]

    # Sort files alphabetically by their names for predictable ordering
    png_files.sort()

    # Print the sorted list of files for verification
    print("Sorted files:")
    for file in png_files:
        print(file)

    # Initialize counters and track previous file base name
    prev_base_name = None
    count = 1

    # Renumerate files with updated sequence numbers
    for filename in png_files:
        base_name = get_base_name(filename)

        # Reset counter when base name changes
        if base_name != prev_base_name:
            count = 1

        new_filename = f"{base_name}{count:03d}.png"
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
        print(f"Renaming {filename} to {new_filename}")

        # Update trackers
        prev_base_name = base_name
        count += 1
