import unittest
import os
import tempfile


class TestRenameFilesInFolder(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for the test
        self.test_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        # Clean up the temporary directory after each test
        self.test_dir.cleanup()

    def test_files_with_colons(self):
        # Create files with colons in their names
        filenames = ['file:one.txt', 'file:two.txt', 'file:three.txt']
        for name in filenames:
            open(os.path.join(self.test_dir.name, name), 'a').close()

        rename_files_in_folder(self.test_dir.name)

        # Check if files were renamed correctly
        expected_files = ['file-one.txt', 'file-two.txt', 'file-three.txt']
        result_files = os.listdir(self.test_dir.name)
        self.assertCountEqual(result_files, expected_files)

    def test_files_without_colons(self):
        # Create files without colons in their names
        filenames = ['file1.txt', 'file2.txt', 'file3.txt']
        for name in filenames:
            open(os.path.join(self.test_dir.name, name), 'a').close()

        rename_files_in_folder(self.test_dir.name)

        # Check that file names remain unchanged
        result_files = os.listdir(self.test_dir.name)
        self.assertCountEqual(result_files, filenames)

    def test_mixed_files(self):
        # Create a mix of files with and without colons
        filenames = ['file:one.txt', 'file2.txt', 'file:three.txt']
        for name in filenames:
            open(os.path.join(self.test_dir.name, name), 'a').close()

        rename_files_in_folder(self.test_dir.name)

        # Check if only the files with colons were renamed
        expected_files = ['file-one.txt', 'file2.txt', 'file-three.txt']
        result_files = os.listdir(self.test_dir.name)
        self.assertCountEqual(result_files, expected_files)

    def test_empty_directory(self):
        # The directory is empty
        rename_files_in_folder(self.test_dir.name)

        # Check that the directory is still empty
        result_files = os.listdir(self.test_dir.name)
        self.assertEqual(len(result_files), 0)

    def test_subdirectories(self):
        # Create a subdirectory and files within the test directory
        os.mkdir(os.path.join(self.test_dir.name, 'subdir'))
        filenames = ['file:one.txt', 'subdir/file:two.txt']
        open(os.path.join(self.test_dir.name, filenames[0]), 'a').close()
        open(os.path.join(self.test_dir.name, filenames[1]), 'a').close()

        rename_files_in_folder(self.test_dir.name)

        # Check if only the file in the main directory was renamed
        expected_files_main = ['file-one.txt', 'subdir']
        result_files_main = os.listdir(self.test_dir.name)
        result_files_subdir = os.listdir(os.path.join(self.test_dir.name, 'subdir'))

        self.assertCountEqual(result_files_main, expected_files_main)
        self.assertCountEqual(result_files_subdir, ['file:two.txt'])  # Should remain unchanged
