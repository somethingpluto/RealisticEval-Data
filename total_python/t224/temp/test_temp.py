import os
import shutil
import tempfile
import unittest


class TestEmptyDirectory(unittest.TestCase):
    def setUp(self):
        # Set up a temporary directory with some files and directories
        self.test_dir = tempfile.mkdtemp()
        # Create some files and directories
        os.mkdir(os.path.join(self.test_dir, 'subdir'))
        with open(os.path.join(self.test_dir, 'file1.txt'), 'w') as f:
            f.write("Hello")
        with open(os.path.join(self.test_dir, 'subdir', 'file2.txt'), 'w') as f:
            f.write("World")

    def tearDown(self):
        # Remove the temporary directory after each test.js
        shutil.rmtree(self.test_dir)

    def test_empty_directory_success(self):
        """ Test that the directory is emptied successfully """
        empty_directory(self.test_dir)
        self.assertEqual(os.listdir(self.test_dir), [])  # Directory should be empty

    def test_non_existing_directory(self):
        """ Test that the correct error is raised when the directory does not exist """
        with self.assertRaises(ValueError) as context:
            empty_directory('/non/existing/directory')
        self.assertTrue("The specified directory does not exist" in str(context.exception))

    def test_not_a_directory(self):
        """ Test that the function raises an error if the path is not a directory """
        # Create a temporary file
        temp_file = tempfile.mktemp()
        with open(temp_file, 'w') as f:
            f.write("Hello")
        try:
            with self.assertRaises(ValueError) as context:
                empty_directory(temp_file)
            self.assertTrue("The specified path is not a directory" in str(context.exception))
        finally:
            os.remove(temp_file)

    def test_empty_directory_with_subdirectories(self):
        """ Test emptying a directory that includes subdirectories """
        empty_directory(self.test_dir)
        self.assertFalse(os.listdir(self.test_dir))  # Directory and subdirectory should be empty

    def test_empty_already_empty_directory(self):
        """ Test emptying a directory that is already empty """
        empty_directory(self.test_dir)  # First emptying
        empty_directory(self.test_dir)  # Empty again
        self.assertEqual(os.listdir(self.test_dir), [])  # Still should be empty

import os
import shutil


def empty_directory(directory_path):
    """
    Empties all files and subdirectories in the specified directory, but keeps the directory itself.

    Args:
    directory_path (str): Path to the directory whose contents are to be emptied.

    Raises:
    ValueError: If the specified path does not exist or is not a directory.
    """
    # Check if the path exists and is a directory
    if not os.path.exists(directory_path):
        raise ValueError("The specified directory does not exist.")
    if not os.path.isdir(directory_path):
        raise ValueError("The specified path is not a directory.")

    # Iterate over all items in the directory
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)

        # Check if the item is a file or directory and delete accordingly
        if os.path.isfile(item_path) or os.path.islink(item_path):
            os.remove(item_path)  # Remove the file or link
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)  # Remove the directory and all its contents
