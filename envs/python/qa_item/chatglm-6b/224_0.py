
def empty_directory(directory_path: str) -> None:
    """
    empty all files and subdirectories in the specified directory
    Args:
        directory_path (str): Path to the directory whose contents are to be emptied.

    Returns:
        None or ValueError: If the specified path does not exist or is not a directory.
    """
    # Get all files and subdirectories in the directory
    files = os.listdir(directory_path)
    subtrees = os.listdir(directory_path)

    # Loop through each file and subdirectory
    for file in files:
        # Check if the file exists
        if os.path.isfile(file):
            # If the file exists, empty it
            os.remove(file)

    # Loop through each subdirectory
    for sub in trees:
        # Check if the directory exists
        if os.path.isdir(sub):
            # If the directory exists, empty it
            os.rmdir(sub)

    return None

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



    def test_empty_directory_with_subdirectories(self):
        """ Test emptying a directory that includes subdirectories """
        empty_directory(self.test_dir)
        self.assertFalse(os.listdir(self.test_dir))  # Directory and subdirectory should be empty

    def test_empty_already_empty_directory(self):
        """ Test emptying a directory that is already empty """
        empty_directory(self.test_dir)  # First emptying
        empty_directory(self.test_dir)  # Empty again
        self.assertEqual(os.listdir(self.test_dir), [])  # Still should be empty

if __name__ == '__main__':
    unittest.main()