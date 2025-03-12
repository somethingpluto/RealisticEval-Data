
from typing import List

def diff_files(file1_path: str, file2_path: str) -> List[str]:
    """
    Compare the contents of two files and print the differences in unified diff format.

    Args:
    file1_path (str): Path to the first file.
    file2_path (str): Path to the second file.

    Returns:
    List[str]: A list containing the lines of differences, if any.

    Raises:
    FileNotFoundError: If either file does not exist.
    IOError: If there is an error reading the files.
    """
    
    # Read the contents of the two files
    with open(file1_path, 'r') as f1, open(file2_path, 'r') as f2:
        content1 = f1.read()
        content2 = f2.read()
        
    # Create a dictionary to store the differences
    diffs = {}
    
    # Iterate over the lines in the two files
    for line1 in content1:
        if line1 not in diffs:
            diffs[line1] = []
        diffs[line1].append(line2)
        
    # Iterate over the lines in the second file
    for line2 in content2:
        if line2 not in diffs:
            diffs[line2] = []
        diffs[line2].append(line1)
        
    # Return the list of differences
    return diffs

import os
import unittest
from unittest.mock import mock_open, patch


class TestCompareFiles(unittest.TestCase):

    def setUp(self):
        # 创建文件用于测试
        self.file1_path = 'file1.txt'
        self.file2_path = 'file2.txt'

    def tearDown(self):
        # 删除创建的文件
        if os.path.exists(self.file1_path):
            os.remove(self.file1_path)
        if os.path.exists(self.file2_path):
            os.remove(self.file2_path)

    def test_identical_files(self):
        # Mock question for two identical files
        file1_content = "Line1\nLine2\nLine3\n"
        file2_content = "Line1\nLine2\nLine3\n"

        with open(self.file1_path, 'w') as f1, open(self.file2_path, 'w') as f2:
            f1.write(file1_content)
            f2.write(file2_content)

        result = diff_files(self.file1_path, self.file2_path)
        self.assertEqual(len(result), 0, "There should be no differences detected")

    def test_files_with_differences(self):
        # Mock question for two different files
        file1_content = "Line1\nLine2\nLine3\n"
        file2_content = "Line1\nLineChanged\nLine3\n"

        with open(self.file1_path, 'w') as f1, open(self.file2_path, 'w') as f2:
            f1.write(file1_content)
            f2.write(file2_content)

        result = diff_files(self.file1_path, self.file2_path)
        self.assertNotEqual(len(result), 0, "There should be differences detected")

    def test_nonexistent_file(self):
        # Test when one of the files does not exist
        with patch('builtins.open', side_effect=FileNotFoundError("File not found")):
            with self.assertRaises(FileNotFoundError):
                diff_files('nonexistent.txt', 'file2.txt')

    def test_file_reading_error(self):
        # Test when there's an error reading the file
        with patch('builtins.open', side_effect=IOError("Error reading file")):
            with self.assertRaises(IOError):
                diff_files('file1.txt', 'file2.txt')

if __name__ == '__main__':
    unittest.main()