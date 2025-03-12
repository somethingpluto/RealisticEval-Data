import re

def is_snake_case(input: str) -> bool:
    """
    Detects whether the string is in SNAKE_CASE.

    In SNAKE_CASE, all letters are lowercase, and words are separated by underscores.
    There should be no leading or trailing underscores, and no spaces or other special characters.

    Args:
        input (str): The string to check.

    Returns:
        bool: True if the string is in SNAKE_CASE, otherwise False.
    """

    if not isinstance(input, str):
        return False

    if not re.match("^[a-z]+(_[a-z]+)*$", input):
        return False

    return True
import unittest


class TestIsSnakeCase(unittest.TestCase):

    def test_valid_snake_case(self):
        """should return true for a valid snake_case string"""
        self.assertTrue(is_snake_case('snake_case'))

    def test_valid_snake_case_multiple_words(self):
        """should return true for a valid snake_case string with multiple words"""
        self.assertTrue(is_snake_case('snake_case_example'))

    def test_uppercase_start(self):
        """should return false for a string that starts with an uppercase letter"""
        self.assertFalse(is_snake_case('Snake_Case'))

    def test_mixed_case_letters(self):
        """should return false for a string with mixed case letters"""
        self.assertFalse(is_snake_case('snakeCASE'))

    def test_string_with_numbers(self):
        """should return false for a string with numbers"""
        self.assertFalse(is_snake_case('snake_case_123'))

    def test_empty_string(self):
        """should return false for an empty string"""
        self.assertFalse(is_snake_case(''))

if __name__ == '__main__':
    unittest.main()