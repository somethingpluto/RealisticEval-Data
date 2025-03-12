
def replace_words_in_file(file_path: str, replacement_dict: dict) -> str:
    with open(file_path, 'r') as f:
        text = f.read()
    
    modified_text = ''
    for word in text.split():
        if word in replacement_dict:
            modified_text += f"{word} { replacement_dict[word]}"
    
    return modified_text
python
original_text = "This is the original text."
 replacement_dict = {'original':'replaced', 'text': 'content'}
modified_text = replace_words_in_file('original_text.txt', replacement_dict)
print(modified_text)  # Output: "This is the replaced text."

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