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