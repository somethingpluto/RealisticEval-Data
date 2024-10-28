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