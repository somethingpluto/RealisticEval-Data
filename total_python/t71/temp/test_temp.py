import unittest
import numpy as np
import os


def read_columns(file_name):
    """
    Reads numerical columns from a file starting from the line after the last line containing '/'.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        numpy.ndarray: A 2D numpy array containing the numerical data.

    Raises:
        ValueError: If the file does not contain any '/' character.
    """
    # Initialize a variable to track the last slash line index
    last_slash_index = None

    with open(file_name) as f:
        lines = f.readlines()

    # Find the index of the last line that contains the "/" character
    for i, line in enumerate(lines):
        if "/" in line:
            last_slash_index = i

    # If no "/" character was found, raise an error
    if last_slash_index is None:
        raise ValueError("File does not contain '/' character")

    # Read the remaining lines in the file, starting from the line after the last "/"
    data_lines = lines[last_slash_index + 1:]

    # Remove any empty lines or lines that start with a comment character
    data_lines = [line.strip() for line in data_lines if line.strip() and not line.strip().startswith('!')]

    # If no valid lines remain, return an empty array
    if not data_lines:
        return np.array([])

    # Get the row and column count by counting the number of columns in the first line
    col_count = len(data_lines[0].split())

    # Create an empty numpy array of the required size
    arr = np.zeros((len(data_lines), col_count))

    # Loop through the lines in the file
    for i, line in enumerate(data_lines):
        # Split the line into numbers and convert them to floats
        nums = [float(x) for x in line.split()]
        # Store the numbers in the array
        arr[i, :] = nums

    # Return the array
    return arr


class TestReadColumns(unittest.TestCase):

    def setUp(self):
        # Setup a temporary directory to use for each test
        self.test_file = 'test_file.txt'

    def tearDown(self):
        # Clean up the temporary file after each test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_basic_functionality(self):
        # Test reading a file with a valid structure and numerical data
        content = """Line 1
Line 2
/
1.0 2.0 3.0
4.0 5.0 6.0
"""
        with open(self.test_file, 'w') as f:
            f.write(content)

        result = read_columns(self.test_file)
        expected_result = np.array([[1.0, 2.0, 3.0],
                                    [4.0, 5.0, 6.0]])
        np.testing.assert_array_equal(result, expected_result)

    def test_no_slash_character(self):
        # Test that a ValueError is raised if no '/' character is found
        content = """Line 1
Line 2
Line 3
"""
        with open(self.test_file, 'w') as f:
            f.write(content)

        with self.assertRaises(ValueError):
            read_columns(self.test_file)

    def test_file_with_comments_and_empty_lines(self):
        # Test handling of comments and empty lines
        content = """Line 1
/
! This is a comment
1.0 2.0 3.0

4.0 5.0 6.0
! Another comment
"""
        with open(self.test_file, 'w') as f:
            f.write(content)

        result = read_columns(self.test_file)
        expected_result = np.array([[1.0, 2.0, 3.0],
                                    [4.0, 5.0, 6.0]])
        np.testing.assert_array_equal(result, expected_result)

    def test_different_number_of_columns(self):
        # Test that the function handles different number of columns correctly
        content = """Line 1
/
1.0 2.0
3.0 4.0
5.0 6.0 7.0
"""
        with open(self.test_file, 'w') as f:
            f.write(content)

        with self.assertRaises(ValueError):
            read_columns(self.test_file)

    def test_empty_file(self):
        # Test handling of an empty file
        content = """"""
        with open(self.test_file, 'w') as f:
            f.write(content)

        with self.assertRaises(ValueError):
            read_columns(self.test_file)

import numpy as np


def read_columns(file_name):
    """
    Reads numerical columns from a file starting from the line after the last line containing '/'.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        numpy.ndarray: A 2D numpy array containing the numerical data.

    Raises:
        ValueError: If the file does not contain any '/' character.
    """
    # Initialize a variable to track the last slash line index
    last_slash_index = None

    with open(file_name) as f:
        lines = f.readlines()

    # Find the index of the last line that contains the "/" character
    for i, line in enumerate(lines):
        if "/" in line:
            last_slash_index = i

    # If no "/" character was found, raise an error
    if last_slash_index is None:
        raise ValueError("File does not contain '/' character")

    # Read the remaining lines in the file, starting from the line after the last "/"
    data_lines = lines[last_slash_index + 1:]

    # Remove any empty lines or lines that start with a comment character
    data_lines = [line.strip() for line in data_lines if line.strip() and not line.strip().startswith('!')]

    # If no valid lines remain, return an empty array
    if not data_lines:
        return np.array([])

    # Get the row and column count by counting the number of columns in the first line
    col_count = len(data_lines[0].split())

    # Create an empty numpy array of the required size
    arr = np.zeros((len(data_lines), col_count))

    # Loop through the lines in the file
    for i, line in enumerate(data_lines):
        # Split the line into numbers and convert them to floats
        nums = [float(x) for x in line.split()]
        # Store the numbers in the array
        arr[i, :] = nums

    # Return the array
    return arr
