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
