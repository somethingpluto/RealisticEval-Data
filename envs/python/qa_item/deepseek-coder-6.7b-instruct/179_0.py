import os
import shutil

def copy_directory(source_dir: str, target_dir: str) -> None:
    """
    Copies all files and subdirectories from the source directory to the target directory.

    Args:
        source_dir (str): The source directory from which files and subdirectories will be copied.
        target_dir (str): The target directory to which files and subdirectories will be copied.

    Returns:
        None
    """
    # Ensure the source directory exists
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"The source directory '{source_dir}' does not exist.")

    # Create the target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Walk through the source directory
    for root, dirs, files in os.walk(source_dir):
        # Create corresponding directories in the target directory
        for dir_name in dirs:
            source_subdir = os.path.join(root, dir_name)
            target_subdir = source_subdir.replace(source_dir, target_dir, 1)
            if not os.path.exists(target_subdir):
                os.makedirs(target_subdir)

        # Copy files to the target directory
        for file_name in files:
            source_file = os.path.join(root, file_name)
            target_file = source_file.replace(source_dir, target_dir, 1)
            shutil.copy2(source_file, target_file)
import os
import shutil
import unittest


class TestDirectoryOperations(unittest.TestCase):

    def setUp(self):
        self.source_dir = "testSourceDir"
        self.target_dir = "testTargetDir"

        os.makedirs(self.source_dir, exist_ok=True)
        os.makedirs(self.target_dir, exist_ok=True)

    def tearDown(self):
        self.delete_directory(self.source_dir)
        self.delete_directory(self.target_dir)

    def delete_directory(self, dir_path):
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)

    def test_copy_empty_directory(self):
        # Simulating Answer.copyDirectory functionality
        copy_directory(self.source_dir, self.target_dir)

        self.assertTrue(os.path.exists(self.target_dir), "Target directory should exist after copying.")
        self.assertTrue(os.path.isdir(self.target_dir), "Target directory should be a directory.")
        self.assertEqual(len(os.listdir(self.target_dir)), 0, "Target directory should be empty.")

    def test_copy_directory_with_files(self):
        test_file = os.path.join(self.source_dir, "testFile.txt")
        with open(test_file, 'w') as f:
            f.write("Sample content")

        copy_directory(self.source_dir, self.target_dir)

        copied_file = os.path.join(self.target_dir, "testFile.txt")
        self.assertTrue(os.path.exists(copied_file), "File should be copied to target directory.")
        self.assertEqual(os.path.getsize(test_file), os.path.getsize(copied_file),
                         "File size should be the same after copying.")

    def test_non_existent_source_directory(self):
        non_existent_dir = "nonExistentDir"

        with self.assertRaises(Exception) as context:
            copy_directory(non_existent_dir, self.target_dir)

        self.assertEqual(str(context.exception), "Source directory does not exist.")

    def test_copy_directory_with_subdirectories(self):
        sub_dir = os.path.join(self.source_dir, "subDir")
        os.makedirs(sub_dir, exist_ok=True)
        test_file = os.path.join(sub_dir, "testFile.txt")
        with open(test_file, 'w') as f:
            f.write("Sample content in subdirectory")

        copy_directory(self.source_dir, self.target_dir)

        copied_sub_dir = os.path.join(self.target_dir, "subDir")
        copied_file = os.path.join(copied_sub_dir, "testFile.txt")

        self.assertTrue(os.path.exists(copied_sub_dir), "Subdirectory should be copied to target directory.")
        self.assertTrue(os.path.exists(copied_file), "File within subdirectory should be copied to target directory.")

    def test_overwrite_file_in_target_directory(self):
        # Create a source file with some content
        test_file = os.path.join(self.source_dir, "testFile.txt")
        with open(test_file, 'w') as f:
            f.write("Source content")

        # Create a target file with different content
        target_file = os.path.join(self.target_dir, "testFile.txt")
        with open(target_file, 'w') as f:
            f.write("Target content")

        # Copy the directory, which should overwrite the target file
        copy_directory(self.source_dir, self.target_dir)

        copied_file = os.path.join(self.target_dir, "testFile.txt")
        self.assertTrue(os.path.exists(copied_file), "File should be copied to target directory.")

        # Check that the content of the file is now the same as the source file
        with open(copied_file, 'r') as f:
            copied_content = f.read()

        self.assertEqual(copied_content, "Source content",
                         "File in target directory should be overwritten with source content.")

if __name__ == '__main__':
    unittest.main()