from typing import List

def split_string(s: str) -> List[str]:
    """
    Split a string into multiple substrings based on spaces and return a list containing these substrings.
    Args:
        s (str): The input string to be split into words.

    Returns:
        List[str]: A list of strings, each representing a word from the input string. Returns an empty list if the input string is empty or contains only spaces.
    """
    # Strip leading and trailing spaces to handle edge cases
    stripped_string = s.strip()
    
    # Check if the stripped string is empty
    if not stripped_string:
        return []
    
    # Split the string by spaces and return the list of words
    return stripped_string.split()
import unittest


class Tester(unittest.TestCase):

    def test_split_string_regular_sentence(self):
        """Split a regular sentence."""
        input_str = "Hello world from Catch2"
        expected = ["Hello", "world", "from", "Catch2"]
        self.assertEqual(split_string(input_str), expected)

    def test_handle_multiple_spaces(self):
        """Handle multiple spaces between words."""
        input_str = "Multiple   spaces between words"
        expected = ["Multiple", "spaces", "between", "words"]
        self.assertEqual(split_string(input_str), expected)

    def test_single_word_input(self):
        """Single word input."""
        input_str = "Single"
        expected = ["Single"]
        self.assertEqual(split_string(input_str), expected)

    def test_empty_string_input(self):
        """Empty string input."""
        input_str = ""
        expected = []
        self.assertEqual(split_string(input_str), expected)

    def test_leading_and_trailing_spaces(self):
        """String with leading and trailing spaces."""
        input_str = "   Leading and trailing spaces   "
        expected = ["Leading", "and", "trailing", "spaces"]
        self.assertEqual(split_string(input_str), expected)

if __name__ == '__main__':
    unittest.main()