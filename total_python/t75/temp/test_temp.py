import os
import unittest
from unittest.mock import patch


class TestRenameFiles(unittest.TestCase):
    @patch('os.listdir')
    @patch('os.rename')
    def test_typical_files(self, mock_rename, mock_listdir):
        mock_listdir.return_value = ['image001.png', 'image002.png', 'image003.png']
        directory = '/fake/directory'
        rename_files(directory)
        calls = [patch.call(os.path.join(directory, 'image001.png'), os.path.join(directory, 'image001.png')),
                 patch.call(os.path.join(directory, 'image002.png'), os.path.join(directory, 'image002.png')),
                 patch.call(os.path.join(directory, 'image003.png'), os.path.join(directory, 'image003.png'))]
        mock_rename.assert_has_calls(calls, any_order=True)

    @patch('os.listdir')
    @patch('os.rename')
    def test_empty_directory(self, mock_rename, mock_listdir):
        mock_listdir.return_value = []
        directory = '/fake/directory'
        rename_files(directory)
        mock_rename.assert_not_called()

    @patch('os.listdir')
    @patch('os.rename')
    def test_complex_file_names(self, mock_rename, mock_listdir):
        mock_listdir.return_value = ['data100-1.png', 'data100-2.png', 'info100-1.png']
        directory = '/fake/directory'
        rename_files(directory)
        expected_calls = [patch.call(os.path.join(directory, 'data100-1.png'), os.path.join(directory, 'data001.png')),
                          patch.call(os.path.join(directory, 'data100-2.png'), os.path.join(directory, 'data002.png')),
                          patch.call(os.path.join(directory, 'info100-1.png'), os.path.join(directory, 'info001.png'))]
        mock_rename.assert_has_calls(expected_calls, any_order=True)

    @patch('os.listdir')
    @patch('os.rename')
    def test_mixed_case_sensitivity(self, mock_rename, mock_listdir):
        mock_listdir.return_value = ['Image001.PNG', 'image002.png', 'IMAGE003.Png']
        directory = '/fake/directory'
        rename_files(directory)
        expected_calls = [patch.call(os.path.join(directory, 'Image001.PNG'), os.path.join(directory, 'Image001.png')),
                          patch.call(os.path.join(directory, 'image002.png'), os.path.join(directory, 'image002.png')),
                          patch.call(os.path.join(directory, 'IMAGE003.Png'), os.path.join(directory, 'IMAGE003.png'))]
        mock_rename.assert_has_calls(expected_calls, any_order=True)

    @patch('os.listdir')
    @patch('os.rename')
    def test_sequential_renaming_reset(self, mock_rename, mock_listdir):
        mock_listdir.return_value = ['set101.png', 'set102.png', 'newset101.png']
        directory = '/fake/directory'
        rename_files(directory)
        expected_calls = [patch.call(os.path.join(directory, 'set101.png'), os.path.join(directory, 'set001.png')),
                          patch.call(os.path.join(directory, 'set102.png'), os.path.join(directory, 'set002.png')),
                          patch.call(os.path.join(directory, 'newset101.png'), os.path.join(directory, 'newset001.png'))]
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
