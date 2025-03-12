import re

class WordDistance:
    def __init__(self, file_path):
        self.file_path = file_path
        self.words = []
        self.word_indices = {}

    def calculate_distance(self, word1, word2):
        if word1 not in self.word_indices or word2 not in self.word_indices:
            return -1

        indices1 = self.word_indices[word1]
        indices2 = self.word_indices[word2]

        min_distance = float('inf')
        line_number = -1

        for index1 in indices1:
            for index2 in indices2:
                distance = abs(index1 - index2)
                if distance < min_distance:
                    min_distance = distance
                    line_number = self.words[index1][1]

        return line_number

    def get_min_distance(self, word1, word2):
        with open(self.file_path, 'r') as file:
            line_number = 1
            for line in file:
                words = re.findall(r'\w+', line)
                for word in words:
                    self.words.append((word, line_number))
                    if word in self.word_indices:
                        self.word_indices[word].append(len(self.words) - 1)
                    else:
                        self.word_indices[word] = [len(self.words) - 1]
                line_number += 1

        return self.calculate_distance(word1, word2)
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