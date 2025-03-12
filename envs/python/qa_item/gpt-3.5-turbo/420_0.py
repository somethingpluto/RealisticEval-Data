import os

class WordDistanceFinder:
    def __init__(self, file_path):
        self.file_path = file_path
        self.word_positions = {}

    def _read_file(self):
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
            for line_number, line in enumerate(lines):
                words = line.strip().split()
                for position, word in enumerate(words):
                    if word in self.word_positions:
                        self.word_positions[word].append((line_number, position))
                    else:
                        self.word_positions[word] = [(line_number, position)]

    def get_min_distance(self, word1, word2):
        if not self.word_positions:
            self._read_file()

        if word1 not in self.word_positions or word2 not in self.word_positions:
            return "Words not found in the file"

        min_distance = float('inf')
        min_distance_line = None

        for pos1 in self.word_positions[word1]:
            for pos2 in self.word_positions[word2]:
                distance = abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
                if distance < min_distance:
                    min_distance = distance
                    min_distance_line = pos1[0]

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