from typing import str

def truncate_string_with_replacement(s: str, max_length: int) -> str:
    if len(s) <= max_length:
        return s
    else:
        return s[:max_length-3] + "..."
import unittest


class TestTruncateStringWithReplacement(unittest.TestCase):

    def test_should_return_original_string_if_shorter_than_max_length(self):
        result = truncate_string_with_replacement('Hello World', 20)
        self.assertEqual(result, 'Hello World')

    def test_should_truncate_string_and_replace_excess_with_ellipsis(self):
        result = truncate_string_with_replacement('This is a long string that needs to be truncated.', 20)
        self.assertEqual(result, 'This is a long str...')

    def test_should_truncate_string_at_max_length_and_add_ellipsis(self):
        result = truncate_string_with_replacement('Short string', 10)
        self.assertEqual(result, 'Short str...')

    def test_should_handle_empty_string_correctly(self):
        result = truncate_string_with_replacement('', 10)
        self.assertEqual(result, '')

    def test_should_return_original_string_when_max_length_equals_string_length(self):
        result = truncate_string_with_replacement('Exact length', 12)
        self.assertEqual(result, 'Exact length')

    def test_should_replace_excess_with_ellipsis_in_string_with_special_characters(self):
        result = truncate_string_with_replacement('This string has special characters: !@#$%^&*()', 30)
        self.assertEqual(result, 'This string has special c...')

    def test_should_return_ellipsis_only_when_max_length_is_0(self):
        result = truncate_string_with_replacement('Hello, world!', 0)
        self.assertEqual(result, '...')

if __name__ == '__main__':
    unittest.main()