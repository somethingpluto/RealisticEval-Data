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
