import unittest
import os
import shutil


class TestRenameFilesInDirectory(unittest.TestCase):

    def setUp(self):
        """Setup a temporary directory with sample files."""
        self.test_dir = 'test_directory'
        os.makedirs(self.test_dir, exist_ok=True)
        # Create files with colons in their names
        open(os.path.join(self.test_dir, 'file:1.txt'), 'a').close()
        open(os.path.join(self.test_dir, 'document:2.txt'), 'a').close()
        open(os.path.join(self.test_dir, 'image:3.jpg'), 'a').close()

    def tearDown(self):
        """Clean up by removing the directory created for the test."""
        shutil.rmtree(self.test_dir)

    def test_rename_files(self):
        """Test renaming files from colons to hyphens."""
        rename_files_in_directory(self.test_dir)
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'file-1.txt')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'document-2.txt')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'image-3.jpg')))

    def test_no_colon_files(self):
        """Test directory with files that don't need renaming."""
        # First clean existing files
        shutil.rmtree(self.test_dir)
        os.makedirs(self.test_dir)
        open(os.path.join(self.test_dir, 'file1.txt'), 'a').close()
        rename_files_in_directory(self.test_dir)
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'file1.txt')))

    def test_empty_directory(self):
        """Test an empty directory."""
        # Clear the directory first
        shutil.rmtree(self.test_dir)
        os.makedirs(self.test_dir)
        rename_files_in_directory(self.test_dir)  # Should not raise any errors
        self.assertEqual(len(os.listdir(self.test_dir)), 0)

    def test_invalid_directory(self):
        """Test with an invalid directory path."""
        with self.assertRaises(ValueError):
            rename_files_in_directory('non_existent_directory')

    def test_permission_error(self):
        """Test the behavior when there's a permission issue."""
        # Create a file and make it read-only
        file_path = os.path.join(self.test_dir, 'readonly:file.txt')
        open(file_path, 'a').close()
        os.chmod(file_path, 0o400)  # Make it read-only
        with self.assertRaises(PermissionError):
            rename_files_in_directory(self.test_dir)
        os.chmod(file_path, 0o666)  # Reset permissions for cleanup

import os


def rename_files_in_directory(directory):
    """
    Rename all files in the specified directory by replacing colons in the filenames with hyphens.

    Args:
    directory (str): The path to the directory containing the files to be renamed.
    """
    # Check if the directory exists
    if not os.path.isdir(directory):
        raise ValueError(f"The specified directory does not exist: {directory}")

    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        # Construct the full file path
        file_path = os.path.join(directory, filename)

        # Check if it's a file (not a directory or link etc.)
        if os.path.isfile(file_path):
            # Replace colons in the filename with hyphens
            new_filename = filename.replace(':', '-')

            # Construct the new file path
            new_file_path = os.path.join(directory, new_filename)

            # Rename the file
            os.rename(file_path, new_file_path)
            print(f"Renamed '{filename}' to '{new_filename}'")
