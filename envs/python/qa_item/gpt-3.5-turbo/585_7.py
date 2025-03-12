from re import search

def is_camel_case(input: str) -> bool:
    return bool(search(r'^[a-z]+(?:[A-Z][a-z]+)*$', input))
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