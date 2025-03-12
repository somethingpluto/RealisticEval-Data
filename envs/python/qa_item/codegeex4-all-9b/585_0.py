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

    # Check if the first character is lowercase
    if not input[0].islower():
        return False

    # Check that all other characters are either lowercase or uppercase
    for i in range(1, len(input)):
        if not input[i].islower() and not input[i].isupper():
            return False

        # Check that the first character of each subsequent word is uppercase
        if input[i].isupper() and input[i-1].isupper():
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