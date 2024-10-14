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
