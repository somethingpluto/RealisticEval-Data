import re

class MinDistanceFinder:
    def __init__(self, file_path, word1, word2):
        self.file_path = file_path
        self.word1 = word1
        self.word2 = word2

    def get_min_distance(self):
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
        
        min_distance = float('inf')
        min_distance_line = None

        for i, line in enumerate(lines):
            words = re.findall(r'\b\w+\b', line)
            if self.word1 in words and self.word2 in words:
                index1 = words.index(self.word1)
                index2 = words.index(self.word2)
                distance = abs(index1 - index2)
                if distance < min_distance:
                    min_distance = distance
                    min_distance_line = i + 1
        
        return min_distance, min_distance_line
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