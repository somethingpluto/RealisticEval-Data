def is_snake_case(input: str) -> bool:
    if not input:
        return False
    if input != input.lower():
        return False
    if input != input.replace("_", ""):
        return False
    if input[0] == '_' or input[-1] == '_':
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