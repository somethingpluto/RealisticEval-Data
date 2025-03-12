import difflib

class MinDistanceFinder:
    def __init__(self, file_path):
        self.file_path = file_path
        self.lines = []

    def read_file(self):
        with open(self.file_path, 'r') as f:
            self.lines = [line.strip() for line in f.readlines()]

    def get_min_distance(self, word1, word2):
        if not self.lines:
            self.read_file()

        min_distance = float('inf')
        min_line_number = -1

        for i, line in enumerate(self.lines):
            distance = difflib.get_close_matches(word1, line.split(), n=1, cutoff=0.8)[0] if word1 else 0
            distance += difflib.get_close_matches(word2, line.split(), n=1, cutoff=0.8)[0] if word2 else 0
            if distance < min_distance:
                min_distance = distance
                min_line_number = i + 1

        return min_line_number + 1
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