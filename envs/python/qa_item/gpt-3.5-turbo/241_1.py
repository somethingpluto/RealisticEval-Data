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
    min_distance = float('inf')
    min_line_num = None

    with open(file_path, 'r') as file:
        for line_num, line in enumerate(file, 1):
            if word1 in line and word2 in line:
                words = line.split()
                indexes_word1 = [i for i, word in enumerate(words) if word == word1]
                indexes_word2 = [i for i, word in enumerate(words) if word == word2]

                for index_word1 in indexes_word1:
                    for index_word2 in indexes_word2:
                        distance = abs(index_word1 - index_word2)
                        if distance < min_distance:
                            min_distance = distance
                            min_line_num = line_num

    if min_line_num is None:
        return None, float('inf')
    
    return min_line_num, min_distance
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