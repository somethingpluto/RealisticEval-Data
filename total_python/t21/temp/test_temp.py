import unittest
from unittest.mock import mock_open, patch


class TestCompareFiles(unittest.TestCase):
    def test_identical_files(self):
        # Mock data for two identical files
        file1_content = "Line1\nLine2\nLine3\n"
        file2_content = "Line1\nLine2\nLine3\n"
        mocker = mock_open(read_data=file1_content)
        mocker.side_effect = [mocker.return_value, mock_open(read_data=file2_content).return_value]
        with patch('builtins.open', mocker):
            result = compare_files('file1.txt', 'file2.txt')
            self.assertEqual(len(result), 0, "There should be differences detected")

    def test_files_with_differences(self):
        # Mock data for two different files
        file1_content = "Line1\nLine2\nLine3\n"
        file2_content = "Line1\nLineChanged\nLine3\n"
        mocker = mock_open(read_data=file1_content)
        mocker.side_effect = [mocker.return_value, mock_open(read_data=file2_content).return_value]
        with patch('builtins.open', mocker):
            result = compare_files('file1.txt', 'file2.txt')
            self.assertNotEqual(len(result), 0, "There should be differences detected")

    def test_nonexistent_file(self):
        # Test when one of the files does not exist
        with patch('builtins.open', side_effect=FileNotFoundError("File not found")):
            with self.assertRaises(FileNotFoundError):
                compare_files('nonexistent.txt', 'file2.txt')

    def test_file_reading_error(self):
        # Test when there's an error reading the file
        with patch('builtins.open', side_effect=IOError("Error reading file")):
            with self.assertRaises(IOError):
                compare_files('file1.txt', 'file2.txt')

    def test_multiple_lines_of_differences(self):
        # Test files with multiple differences
        file1_content = "Line1\nLine2\nLine3\nLine4\n"
        file2_content = "Line1\nLine2 changed\nLine3\nLine4 modified\n"
        mocker = mock_open(read_data=file1_content)
        mocker.side_effect = [mocker.return_value, mock_open(read_data=file2_content).return_value]
        with patch('builtins.open', mocker):
            result = compare_files('file1.txt', 'file2.txt')
            self.assertTrue(len(result) > 1, "Multiple differences should be reported")

import difflib


def compare_files(file1_path, file2_path):
    """
    Compare the contents of two files and print the differences in unified diff format.

    Args:
    file1_path (str): Path to the first file.
    file2_path (str): Path to the second file.

    Returns:
    list: A list containing the lines of differences, if any.

    Raises:
    FileNotFoundError: If either file does not exist.
    IOError: If there is an error reading the files.
    """
    try:
        with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
            lines1 = file1.readlines()
            lines2 = file2.readlines()
    except FileNotFoundError:
        raise FileNotFoundError("One of the files was not found.")
    except IOError as e:
        raise IOError(f"Error reading files: {e}")

    diff = difflib.unified_diff(lines1, lines2, fromfile=file1_path, tofile=file2_path)
    diff_lines = list(diff)

    for line in diff_lines:
        print(line, end="")

    return diff_lines
