class WordDistanceFinder:
    def get_min_distance(self, file_path, word1, word2):
        """
        Find the minimum distance between two specified words (word1 and word2) from the file and return in which line the distance occurred

        Args:
            file_path (str): The path to the file containing the text
            word1 (str): The first word to find
            word2 (str): The second word to find

        Returns:
            int: The minimum distance between word1 and word2
            int: The line number where the minimum distance occurred
        """
        min_distance = float('inf')
        min_line = -1
        word1_positions = []
        word2_positions = []

        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                words = line.split()
                for word_index, word in enumerate(words):
                    if word == word1:
                        word1_positions.append((line_number, word_index))
                    elif word == word2:
                        word2_positions.append((line_number, word_index))

                for pos1 in word1_positions:
                    for pos2 in word2_positions:
                        distance = abs(pos1[1] - pos2[1])
                        if distance < min_distance:
                            min_distance = distance
                            min_line = pos1[0]

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