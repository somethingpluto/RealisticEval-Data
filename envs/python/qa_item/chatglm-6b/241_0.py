
from typing import Tuple

def get_min_seq_num_and_distance(file_path: str, word1: str, word2: str) -> Tuple[int, int]:
    """
    Finds the minimum distance between two words in a text file, considering each line as a separate sequence.
    Args:
        file_path (str): The path to the file to read.
        word1 (str): The first word to search for.
        word2 (str): The second word to search for.

    Returns:
        tuple: A tuple containing the line number with the minimum distance and the minimum distance itself.
          Returns (None, float('inf')) if one or both words are not found in any line.
    """
    # Read the file and store the lines in a list
    lines = [line for line in open(file_path, 'r') if line.strip()]

    # Initialize the minimum distance and the line number
    min_distance = float('inf')
    line_num = 0

    # Loop through the lines and find the minimum distance between the two words
    for line in lines:
        line_num += 1
        if word1 in line and word2 in line:
            min_distance = min(min_distance, distance.find(word1, line) + distance.find(word2, line))
        elif word1 in line and not word2 in line:
            min_distance = min(min_distance, distance.find(word1, line))
        else:
            min_distance = min(min_distance, distance.find(word2, line))

    # Return the line number and the minimum distance
    return line_num, min_distance

import unittest
from unittest.mock import mock_open, patch


class TestGetMinDistance(unittest.TestCase):

    def test_basic_functionality(self):
        """ Test basic functionality with expected input """
        mock_content = "hello world\napple banana apple\norange apple banana"
        with patch('builtins.open', mock_open(read_data=mock_content)):
            line_number, distance = get_min_seq_num_and_distance('dummy_file.txt', 'apple', 'banana')
            self.assertEqual((line_number, distance), (2, 1))


    def test_words_not_present(self):
        """ Test case where one or both words are not present """
        mock_content = "apple orange pear\norange pear apple"
        with patch('builtins.open', mock_open(read_data=mock_content)):
            line_number, distance = get_min_seq_num_and_distance('dummy_file.txt', 'apple', 'banana')
            self.assertEqual((line_number, distance), (None, float('inf')))

    def test_empty_file(self):
        """ Test an empty file """
        with patch('builtins.open', mock_open(read_data='')):
            line_number, distance = get_min_seq_num_and_distance('dummy_file.txt', 'apple', 'banana')
            self.assertEqual((line_number, distance), (None, float('inf')))

    def test_multiple_lines_with_varying_distances(self):
        """ Test multiple lines with varying distances between words """
        mock_content = "apple banana\napple orange orange banana\napple orange orange orange banana"
        with patch('builtins.open', mock_open(read_data=mock_content)):
            line_number, distance = get_min_seq_num_and_distance('dummy_file.txt', 'apple', 'banana')
            self.assertEqual((line_number, distance), (1, 1))
if __name__ == '__main__':
    unittest.main()