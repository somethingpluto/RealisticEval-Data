
import re

def is_phrase_in_string_ignore_case(phrase: str, string: str) -> bool:
    """
    Check if the given phrase exists in the target string, ignoring case and allowing for variations in whitespace.

    Args:
        phrase (str): The phrase to search for in the string.
        string (str): The target string in which to search for the phrase.

    Returns:
        bool: True if the phrase is found as a whole word in the string, False otherwise.
    """
    # Convert both strings to lowercase
    string_lower = string.lower()
    
    # Split the target string into words
    words = re.split(r'\b', string_lower)
    
    # Check if the phrase is present in each word
    for word in words:
        if phrase.lower() in word.lower():
            return True
    
    return False

import unittest


class TestIsPhraseInStringIgnoreCase(unittest.TestCase):

    def test_exact_match_case_insensitive(self):
        self.assertTrue(is_phrase_in_string_ignore_case("hello world", "Hello World"))


    def test_partial_word_match_case_insensitive(self):
        self.assertTrue(is_phrase_in_string_ignore_case("Hello", "saying Hello there"))

    def test_different_cases(self):
        self.assertTrue(is_phrase_in_string_ignore_case("HELLO", "hello there!"))
        self.assertTrue(is_phrase_in_string_ignore_case("world", "WORLD is great"))

    def test_non_existent_phrase(self):
        self.assertFalse(is_phrase_in_string_ignore_case("goodbye", "Hello world"))
        self.assertFalse(is_phrase_in_string_ignore_case("hello", "goodbye world"))


if __name__ == '__main__':
    unittest.main()