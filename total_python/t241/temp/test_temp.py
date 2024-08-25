import unittest
from unittest.mock import mock_open, patch


class TestGetMinDistance(unittest.TestCase):

    def test_basic_functionality(self):
        """ Test basic functionality with expected input """
        mock_content = "hello world\napple banana apple\norange apple banana"
        with patch('builtins.open', mock_open(read_data=mock_content)):
            line_number, distance = get_min_seq_num_and_distance('dummy_file.txt', 'apple', 'banana')
            self.assertEqual((line_number, distance), (1, 1))

    def test_words_on_same_line_multiple_times(self):
        """ Test where words appear multiple times on the same line """
        mock_content = "apple apple banana apple banana banana"
        with patch('builtins.open', mock_open(read_data=mock_content)):
            line_number, distance = get_min_seq_num_and_distance('dummy_file.txt', 'apple', 'banana')
            self.assertEqual((line_number, distance), (0, 1))

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
            self.assertEqual((line_number, distance), (0, 1))

def get_min_seq_num_and_distance(file_path, word1, word2):
    """
    Finds the minimum distance between two words in a text file, considering each line as a separate sequence.

    Parameters:
    file_path (str): The path to the file to read.
    word1 (str): The first word to search for.
    word2 (str): The second word to search for.

    Returns:
    tuple: A tuple containing the line number with the minimum distance and the minimum distance itself.
          Returns (None, float('inf')) if one or both words are not found in any line.
    """
    min_distance = float('inf')
    min_seq_num = None
    current_line_number = 0

    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.strip().split()
                word1_indices = [index for index, word in enumerate(words) if word == word1]
                word2_indices = [index for index, word in enumerate(words) if word == word2]

                for index1 in word1_indices:
                    for index2 in word2_indices:
                        distance = abs(index1 - index2)
                        if distance < min_distance:
                            min_distance = distance
                            min_seq_num = current_line_number

                current_line_number += 1

    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return None, float('inf')
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, float('inf')

    return min_seq_num, min_distance
