import os

def replace_words_in_file(file_path: str, replacement_dict: dict) -> str:
    """
    Read a text file, replace words according to a dictionary map, and return the modified text.

    Parameters:
    - file_path (str): The path to the text file.
    - replacement_dict (dict): A dictionary where the keys are words to be replaced, and the values are the replacement words.

    Returns:
    - str: The text with the words replaced.
    """
    if not os.path.isfile(file_path):
        return "File not found"

    with open(file_path, 'r') as file:
        text = file.read()

    for key, value in replacement_dict.items():
        text = text.replace(key, value)

    return text
import unittest
from unittest.mock import mock_open, patch


class TestReplaceWordsInFile(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="hello world")
    def test_replace_single_word(self, mock_file):
        file_path = "dummy_path.txt"
        replacement_dict = {"hello": "hi"}
        expected_output = "hi world"

        result = replace_words_in_file(file_path, replacement_dict)
        self.assertEqual(result, expected_output)

    @patch("builtins.open", new_callable=mock_open, read_data="hello world")
    def test_replace_multiple_words(self, mock_file):
        file_path = "dummy_path.txt"
        replacement_dict = {"hello": "hi", "world": "earth"}
        expected_output = "hi earth"

        result = replace_words_in_file(file_path, replacement_dict)
        self.assertEqual(result, expected_output)

    @patch("builtins.open", new_callable=mock_open, read_data="hello world")
    def test_no_replacement(self, mock_file):
        file_path = "dummy_path.txt"
        replacement_dict = {"goodbye": "bye"}
        expected_output = "hello world"

        result = replace_words_in_file(file_path, replacement_dict)
        self.assertEqual(result, expected_output)

    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_empty_file(self, mock_file):
        file_path = "dummy_path.txt"
        replacement_dict = {"hello": "hi"}
        expected_output = ""

        result = replace_words_in_file(file_path, replacement_dict)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()