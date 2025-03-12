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
    # Open the file in read mode
    with open(file_path, 'r') as file:
        min_distance = float('inf')
        min_line_number = None
        line_number = 0
        
        # Iterate through each line in the file
        for line in file:
            line_number += 1
            words = line.split()
            
            # Check if both words are present in the line
            if word1 in words and word2 in words:
                distance = abs(words.index(word1) - words.index(word2))
                
                # Update minimum distance and line number if the current distance is smaller
                if distance < min_distance:
                    min_distance = distance
                    min_line_number = line_number
                    
        # Return the tuple with the minimum distance and line number
        return (min_line_number, min_distance) if min_line_number is not None else (None, float('inf'))
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