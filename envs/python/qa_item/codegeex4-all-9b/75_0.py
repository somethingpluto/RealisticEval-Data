import os

def rename_png_files_in_directory(directory: str):
    """
    Renames PNG files in a specified directory by appending a sequence number to each file.
    The files are sorted alphabetically, and each base name is assigned sequential numbers.
    For example:
        director have three PNG files such as "image1.png", "image2.png", "image3.png"
        after renaming PNG files are "image1001.png", "image2001.png", "image3001.png"

    Args:
        directory (str): The path to the directory containing PNG files to be renamed.

    Returns:
        None
    """
    # Get a list of all files in the directory
    files = os.listdir(directory)
    
    # Filter out only the PNG files
    png_files = [f for f in files if f.lower().endswith('.png')]
    
    # Sort the PNG files alphabetically
    png_files.sort()
    
    # Create a mapping from old file names to new file names
    new_names = {}
    for i, old_name in enumerate(png_files, start=1):
        base_name, extension = os.path.splitext(old_name)
        new_name = f"{base_name}{i:04d}{extension}"
        new_names[old_name] = new_name
    
    # Rename the files
    for old_name, new_name in new_names.items():
        old_path = os.path.join(directory, old_name)
        new_path = os.path.join(directory, new_name)
        os.rename(old_path, new_path)
import re
import unittest
import os
import shutil
import tempfile
from pathlib import Path



class TestRenameFiles(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for each test
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove the temporary directory after each test
        shutil.rmtree(self.test_dir)

    def create_png_files(self, filenames):
        for filename in filenames:
            file_path = Path(self.test_dir) / filename
            file_path.touch()  # Create an empty file

    def test_basic_renaming(self):
        # Test renaming in a basic scenario with simple filenames
        filenames = ["image1.png", "image2.png", "image3.png"]
        self.create_png_files(filenames)

        rename_png_files_in_directory(self.test_dir)

        expected_files = ['image1001.png', 'image2001.png', 'image3001.png']
        result_files = sorted(os.listdir(self.test_dir))
        self.assertEqual(result_files, expected_files)

    def test_reset_counter_for_different_base_names(self):
        # Test that the counter resets for different base names
        filenames = ["image1.png", "picture1.png", "image2.png", "picture2.png"]
        self.create_png_files(filenames)

        rename_png_files_in_directory(self.test_dir)

        expected_files = ['image1001.png', 'image2001.png', 'picture1001.png', 'picture2001.png']
        result_files = sorted(os.listdir(self.test_dir))
        self.assertEqual(result_files, expected_files)

    def test_no_png_files(self):
        # Test handling of directories with no PNG files
        filenames = ["file1.txt", "file2.jpg"]
        self.create_png_files(filenames)

        rename_png_files_in_directory(self.test_dir)

        expected_files = filenames  # No changes expected
        result_files = sorted(os.listdir(self.test_dir))
        self.assertEqual(result_files, expected_files)

    def test_empty_directory(self):
        # Test handling of an empty directory
        rename_png_files_in_directory(self.test_dir)
        expected_files = []  # No files to rename
        result_files = os.listdir(self.test_dir)
        self.assertEqual(result_files, expected_files)

    def test_files_with_existing_numbers(self):
        # Test renaming files that already have numbers in their names
        filenames = ["file001.png", "file002.png", "file003.png"]
        self.create_png_files(filenames)

        rename_png_files_in_directory(self.test_dir)

        expected_files = ['file001001.png', 'file002001.png', 'file003001.png']
        result_files = sorted(os.listdir(self.test_dir))
        self.assertEqual(result_files, expected_files)
if __name__ == '__main__':
    unittest.main()