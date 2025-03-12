
def rename_png_files_in_directory(directory: str):
    # Get a list of all the PNG files in the directory
    png_files = [f for f in os.listdir(directory) if f.endswith(".png")]

    # Sort the list of PNG files alphabetically
    png_files.sort()

    # Create a new list to store the new names of the PNG files
    new_names = []

    # Loop through each PNG file in the list
    for png_file in png_files:
        # Get the base name of the PNG file
        base_name = png_file.split("/")[-1]

        # Get the sequence number for the PNG file
        sequence_number = int(os.path.splitext(base_name)[0])

        # Add the sequence number to the new name of the PNG file
        new_name = f"{base_name[:-4]}_{sequence_number}.png"
        new_names.append(new_name)

    # Return the new list of names of the PNG files
    return new_names
python
new_names = rename_png_files_in_directory("director")

import re
import unittest
import os
import shutil
import tempfile
from pathlib import Path



class TestRenameFiles(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def create_png_files(self, filenames):
        for filename in filenames:
            file_path = Path(self.test_dir) / filename
            file_path.touch()  # Create an empty file

    def test_basic_renaming(self):
        filenames = ["image1.png", "image2.png", "image3.png"]
        self.create_png_files(filenames)

        rename_png_files_in_directory(self.test_dir)

        expected_files = ['image1001.png', 'image2001.png', 'image3001.png']
        result_files = sorted(os.listdir(self.test_dir))
        self.assertEqual(result_files, expected_files)

    def test_reset_counter_for_different_base_names(self):
        filenames = ["image1.png", "picture1.png", "image2.png", "picture2.png"]
        self.create_png_files(filenames)

        rename_png_files_in_directory(self.test_dir)

        expected_files = ['image1001.png', 'image2001.png', 'picture1001.png', 'picture2001.png']
        result_files = sorted(os.listdir(self.test_dir))
        self.assertEqual(result_files, expected_files)

    def test_no_png_files(self):
        filenames = ["file1.txt", "file2.jpg"]
        self.create_png_files(filenames)

        rename_png_files_in_directory(self.test_dir)

        expected_files = filenames  # No changes expected
        result_files = sorted(os.listdir(self.test_dir))
        self.assertEqual(result_files, expected_files)

    def test_empty_directory(self):
        rename_png_files_in_directory(self.test_dir)
        expected_files = []  # No files to rename
        result_files = os.listdir(self.test_dir)
        self.assertEqual(result_files, expected_files)

    def test_files_with_existing_numbers(self):
        filenames = ["file001.png", "file002.png", "file003.png"]
        self.create_png_files(filenames)

        rename_png_files_in_directory(self.test_dir)

        expected_files = ['file001001.png', 'file002001.png', 'file003001.png']
        result_files = sorted(os.listdir(self.test_dir))
        self.assertEqual(result_files, expected_files)
if __name__ == '__main__':
    unittest.main()