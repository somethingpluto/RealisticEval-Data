import unittest
from unittest.mock import mock_open, patch
import numpy as np

class TestReadColumns(unittest.TestCase):
    def test_read_valid_content(self):
        """ Test reading from a file with valid content. """
        file_content = "header\n123 / example\n1 2 3\n4 5 6\n! Comment\n"
        m = mock_open(read_data=file_content)
        with patch('builtins.open', m):
            result = read_columns('dummy_file.txt')
            expected_result = np.array([[1, 2, 3], [4, 5, 6]])
            np.testing.assert_array_equal(result, expected_result)

    def test_no_slash_in_file(self):
        """ Test error handling when no '/' is present in the file. """
        file_content = "header\n123 example\n1 2 3\n4 5 6\n"
        m = mock_open(read_data=file_content)
        with patch('builtins.open', m):
            with self.assertRaises(ValueError):
                read_columns('dummy_file.txt')

    def test_file_with_only_slashes(self):
        """ Test reading a file where every line contains '/'. """
        file_content = "/ first line\n/ second line\n/ third line\n1 2 3\n4 5 6\n"
        m = mock_open(read_data=file_content)
        with patch('builtins.open', m):
            result = read_columns('dummy_file.txt')
            expected_result = np.array([[1, 2, 3], [4, 5, 6]])
            np.testing.assert_array_equal(result, expected_result)

    def test_file_with_comments_after_slash(self):
        """ Test file handling with comments after the last '/'. """
        file_content = "header\n/ last relevant\n1 2 3\n! Comment\n4 5 6\n"
        m = mock_open(read_data=file_content)
        with patch('builtins.open', m):
            result = read_columns('dummy_file.txt')
            expected_result = np.array([[1, 2, 3], [4, 5, 6]])
            np.testing.assert_array_equal(result, expected_result)

    def test_empty_lines_after_last_slash(self):
        """ Test the handling of empty lines after the last '/'. """
        file_content = "header\n/ last relevant\n\n\n1 2 3\n4 5 6\n"
        m = mock_open(read_data=file_content)
        with patch('builtins.open', m):
            result = read_columns('dummy_file.txt')
            expected_result = np.array([[1, 2, 3], [4, 5, 6]])
            np.testing.assert_array_equal(result, expected_result)
import numpy as np


def read_columns(file_name):
    "Entirely written by ChatGPT."
    # Open the file for reading
    with open(file_name) as f:
        # Find the index of the last line that contains the "/" character
        last_slash_index = None
        for i, line in enumerate(f):
            if "/" in line:
                last_slash_index = i

        # If no "/" character was found, raise an error
        if last_slash_index is None:
            raise ValueError("File does not contain '/' character")

        # Read the remaining lines in the file, starting from the last "/"
        f.seek(0)
        lines = f.readlines()[last_slash_index+1:]

        # Remove any empty lines or comments
        lines = [line for line in lines if line.strip() and not line.strip().startswith('!')]

        # Get the row and column count by counting the number of columns in the first line
        col_count = len(lines[0].split())

        # Create an empty numpy array of the required size
        arr = np.zeros((len(lines), col_count))

        # Loop through the lines in the file
        for i, line in enumerate(lines):
            # Split the line into numbers and convert them to floats
            nums = [float(x) for x in line.split()]
            # Store the numbers in the array
            arr[i, :] = nums

    # Return the array
    return arr
