import sys

class MinDistanceFinder:
    def __init__(self):
        pass
    
    def get_min_distance(self, file_path, word1, word2):
        min_distance = sys.maxsize
        line_number = 0
        word1_index = -1
        word2_index = -1
        
        with open(file_path, 'r') as file:
            for line in file:
                line_number += 1
                words = line.split()
                if word1 in words:
                    word1_index = words.index(word1)
                if word2 in words:
                    word2_index = words.index(word2)
                
                if word1_index != -1 and word2_index != -1:
                    distance = abs(word1_index - word2_index)
                    if distance < min_distance:
                        min_distance = distance
                        min_distance_line = line_number
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