import re

def is_camel_case(input: str) -> bool:
    """
    Detects whether the string is in CAMEL_CASE.

    In CAMEL_CASE, the first letter of the first word is lowercase,
    and each subsequent word starts with an uppercase letter, with no spaces or underscores
    separating the words.

    Args:
        input (str): The string to check.

    Returns:
        bool: True if the string is in CAMEL_CASE, otherwise False.
    """
    if not input:
        return False
    
    # Check if first letter is lowercase
    if not input[0].islower():
        return False
    
    # Check if there are any spaces or underscores
    if re.search(r'\s|_', input):
        return False
    
    # Check if each subsequent word starts with an uppercase letter
    words = re.split(r'[A-Z]', input[1:])
    for word in words:
        if word and not word[0].isupper():
            return False
    
    return True
import unittest


class TestIsCamelCase(unittest.TestCase):

    def test_valid_camel_case(self):
        """Should return true for a valid camelCase string."""
        self.assertTrue(is_camel_case('camelCase'))

    def test_valid_camel_case_multiple_words(self):
        """Should return true for a valid camelCase string with multiple words."""
        self.assertTrue(is_camel_case('camelCaseExample'))

    def test_uppercase_start(self):
        """Should return false for a string that starts with an uppercase letter."""
        self.assertFalse(is_camel_case('CamelCase'))

    def test_underscores(self):
        """Should return false for a string with underscores."""
        self.assertFalse(is_camel_case('camel_case'))

    def test_empty_string(self):
        """Should return false for an empty string."""
        self.assertFalse(is_camel_case(''))

if __name__ == '__main__':
    unittest.main()