import sys

class MinDistanceFinder:
    def __init__(self, file_path, word1, word2):
        self.file_path = file_path
        self.word1 = word1
        self.word2 = word2

    def get_min_distance(self):
        min_distance = sys.maxsize
        min_distance_line = None
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
            word1_index = None
            word2_index = None
            for idx, line in enumerate(lines):
                if self.word1 in line:
                    word1_index = idx
                    if word2_index is not None:
                        min_distance = min(min_distance, abs(word1_index - word2_index))
                        if min_distance == abs(word1_index - word2_index):
                            min_distance_line = idx
                if self.word2 in line:
                    word2_index = idx
                    if word1_index is not None:
                        min_distance = min(min_distance, abs(word1_index - word2_index))
                        if min_distance == abs(word1_index - word2_index):
                            min_distance_line = idx

        return min_distance_line, min_distance
import unittest
from unittest.mock import patch


class TestGetMinDistance(unittest.TestCase):
    @patch('builtins.open')
    def test_simple_case(self, mock_open):
        # Mock the file read operation
        mock_open.return_value.__enter__.return_value = iter([
            "hello world",
            "hello hello world",
            "world hello"
        ])
        self.assertEqual(get_min_distance("dummy_file.txt", "hello", "world"), (0, 1))


    @patch('builtins.open')
    def test_multiple_lines(self, mock_open):
        mock_open.return_value.__enter__.return_value = iter([
            "hello planet",
            "world hello planet",
            "hello world planet"
        ])
        self.assertEqual(get_min_distance("dummy_file.txt", "hello", "world"), (1, 1))

    @patch('builtins.open')
    def test_large_distance(self, mock_open):
        mock_open.return_value.__enter__.return_value = iter([
            "hello a b c d e f g h i j k l m n o p q r s t u v w x y z world"
        ])
        self.assertEqual(get_min_distance("dummy_file.txt", "hello", "world"), (0, 27))

    @patch('builtins.open')
    def test_adjacent_words(self, mock_open):
        mock_open.return_value.__enter__.return_value = iter([
            "hello world",
            "hello hello world world",
            "world hello"
        ])
        self.assertEqual(get_min_distance("dummy_file.txt", "hello", "world"), (0, 1))

if __name__ == '__main__':
    unittest.main()