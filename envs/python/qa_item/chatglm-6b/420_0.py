
from ast import Tuple

class MinDistance between Two Words:
    def __init__(self, file_path:str, word1:str, word2:str):
        self.file_path = file_path
        self.word1 = word1
        self.word2 = word2
        self.distance = 0

    def get_min_distance_between_2_words(self, file_path:str, word1:str, word2:str) -> Tuple:
        lines = open(file_path, 'r').readlines()
        for line in lines:
            line_content = line.strip().split(word1)
            if self.word1 in line_content and self.word2 in line_content:
                distance = min(len(line_content[self.word1]), len(line_content[self.word2]))
                self.distance += distance
                print(f"Line {line_content[self.word1]}: {line_content[self.word2]}, Distance: {distance}")
        return self.distance
python
min_distance = MinDistance between Two Words("example.txt", "word1", "word2")
print(min_distance.get_min_distance_between_2_words("example.txt", "word1", "word2"))
csharp
Line example.txt: word1, Distance: 1
Line example.txt: word2, Distance: 1

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
        self.assertEqual(get_min_distance_between_2_word("dummy_file.txt", "hello", "world"), (0, 1))


    @patch('builtins.open')
    def test_multiple_lines(self, mock_open):
        mock_open.return_value.__enter__.return_value = iter([
            "hello planet",
            "world hello planet",
            "hello world planet"
        ])
        self.assertEqual(get_min_distance_between_2_word("dummy_file.txt", "hello", "world"), (1, 1))

    @patch('builtins.open')
    def test_large_distance(self, mock_open):
        mock_open.return_value.__enter__.return_value = iter([
            "hello a b c d e f g h i j k l m n o p q r s t u v w x y z world"
        ])
        self.assertEqual(get_min_distance_between_2_word("dummy_file.txt", "hello", "world"), (0, 27))

    @patch('builtins.open')
    def test_adjacent_words(self, mock_open):
        mock_open.return_value.__enter__.return_value = iter([
            "hello world",
            "hello hello world world",
            "world hello"
        ])
        self.assertEqual(get_min_distance_between_2_word("dummy_file.txt", "hello", "world"), (0, 1))

if __name__ == '__main__':
    unittest.main()