import re

def is_kebab_case(input: str) -> bool:
    """
    Detects whether the string is in KEBAB_CASE.

    KEBAB_CASE is defined as a string that:
    - Contains only lowercase letters (a-z).
    - May contain digits (0-9).
    - Uses hyphens (-) as word separators.
    - Does not start or end with a hyphen.
    - Does not contain consecutive hyphens.

    Args:
        input (str): The string to check.

    Returns:
        bool: True if the string is in KEBAB_CASE, otherwise False.
    """
    # Regular expression to match KEBAB_CASE
    pattern = r'^[a-z0-9]+(-[a-z0-9]+)*$'
    
    # Check if the input matches the pattern
    return bool(re.match(pattern, input))
import unittest


class TestIsKebabCase(unittest.TestCase):

    def test_valid_kebab_case(self):
        """Should return True for a valid kebab-case string."""
        self.assertTrue(is_kebab_case('kebab-case'))

    def test_valid_kebab_case_multiple_words(self):
        """Should return True for a valid kebab-case string with multiple words."""
        self.assertTrue(is_kebab_case('this-is-a-valid-kebab-case'))

    def test_uppercase_letters(self):
        """Should return False for a string with uppercase letters."""
        self.assertFalse(is_kebab_case('Kebab-Case'))

    def test_consecutive_hyphens(self):
        """Should return False for a string with consecutive hyphens."""
        self.assertFalse(is_kebab_case('kebab--case'))

    def test_empty_string(self):
        """Should return False for an empty string."""
        self.assertFalse(is_kebab_case(''))

if __name__ == '__main__':
    unittest.main()