class WordDistance:
    def __init__(self, file_path):
        self.file_path = file_path
        self.lines = self.read_file()

    def read_file(self):
        with open(self.file_path, 'r') as file:
            return file.readlines()

    def get_min_distance(self, word1, word2):
        min_distance = len(self.lines)
        min_line = -1
        word1_index = []
        word2_index = []

        for i, line in enumerate(self.lines):
            words = line.split()
            for j, word in enumerate(words):
                if word == word1:
                    word1_index.append((i, j))
                elif word == word2:
                    word2_index.append((i, j))

        for index1 in word1_index:
            for index2 in word2_index:
                distance = abs(index1[0] - index2[0]) + abs(index1[1] - index2[1])
                if distance < min_distance:
                    min_distance = distance
                    min_line = index1[0]

        return min_distance, min_line
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