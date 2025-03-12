import string

def remove_punctuation(s: str) -> str:
    """
    Removes all punctuation from a given string, converts the string to lowercase,
    and trims whitespace from both ends.

    Args:
        s (str): The string from which to remove punctuation.

    Returns:
        str: The cleaned and formatted string.
    """
    # Remove punctuation
    s = s.translate(str.maketrans('', '', string.punctuation))
    # Convert to lowercase
    s = s.lower()
    # Trim whitespace from both ends
    s = s.strip()
    
    return s
import unittest
import re

class TestRemovePunctuation(unittest.TestCase):

    def test_removes_punctuation_from_simple_sentence(self):
        input_string = "Hello, world!"
        expected = "hello world"
        self.assertEqual(remove_punctuation(input_string), expected)

    def test_handles_string_with_no_punctuation(self):
        input_string = "Hello world"
        expected = "hello world"
        self.assertEqual(remove_punctuation(input_string), expected)

    def test_converts_mixed_case_letters_to_lowercase(self):
        input_string = "HeLLo WoRLd!"
        expected = "hello world"
        self.assertEqual(remove_punctuation(input_string), expected)

    def test_removes_a_variety_of_punctuation(self):
        input_string = "Life, in a nutshell: eat, sleep, code!"
        expected = "life in a nutshell eat sleep code"
        self.assertEqual(remove_punctuation(input_string), expected)

    def test_trims_whitespace_from_ends(self):
        input_string = "   What a wonderful world!   "
        expected = "what a wonderful world"
        self.assertEqual(remove_punctuation(input_string), expected)
if __name__ == '__main__':
    unittest.main()