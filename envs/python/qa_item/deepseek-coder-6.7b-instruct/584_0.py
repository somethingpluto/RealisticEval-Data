def is_pascal_case(input: str) -> bool:
    """
    Detects whether the string is in PASCAL_CASE.

    In PASCAL_CASE, each word starts with an uppercase letter and
    there are no spaces or underscores separating the words.

    Args:
        input (str): The string to check.

    Returns:
        bool: True if the string is in PASCAL_CASE, otherwise False.
    """
    # Check if the input is empty
    if not input:
        return False
    
    # Check if the first character is uppercase
    if not input[0].isupper():
        return False
    
    # Check if the rest of the characters are alphanumeric and lowercase
    for char in input[1:]:
        if not char.isalnum() or char.isupper():
            return False
    
    return True
import unittest


class TestIsPascalCase(unittest.TestCase):

    def test_valid_pascal_case(self):
        """Should return true for a valid PascalCase string."""
        self.assertTrue(is_pascal_case('PascalCase'))

    def test_valid_pascal_case_multiple_words(self):
        """Should return true for a valid PascalCase string with multiple words."""
        self.assertTrue(is_pascal_case('PascalCaseExample'))

    def test_starts_with_lowercase(self):
        """Should return false for a string that starts with a lowercase letter."""
        self.assertFalse(is_pascal_case('pascalCase'))

    def test_with_underscores(self):
        """Should return false for a string with underscores."""
        self.assertFalse(is_pascal_case('Pascal_case'))

    def test_empty_string(self):
        """Should return false for a string that is empty."""
        self.assertFalse(is_pascal_case(''))

if __name__ == '__main__':
    unittest.main()