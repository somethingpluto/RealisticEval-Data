import os

def rename_png_files_in_directory(directory: str):
    file_list = os.listdir(directory)
    png_files = [file for file in file_list if file.lower().endswith('.png')]
    png_files.sort()

    for i, file in enumerate(png_files, start=1):
        base_name, extension = os.path.splitext(file)
        new_name = f"{base_name}{i:03}{extension}"
        os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
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