import unittest


class Tester(unittest.TestCase):

    def test_split_string_regular_sentence(self):
        """Split a regular sentence."""
        input_str = "Hello world from Catch2"
        expected = ["Hello", "world", "from", "Catch2"]
        self.assertEqual(split_string(input_str), expected)

    def test_handle_multiple_spaces(self):
        """Handle multiple spaces between words."""
        input_str = "Multiple   spaces between words"
        expected = ["Multiple", "spaces", "between", "words"]
        self.assertEqual(split_string(input_str), expected)

    def test_single_word_input(self):
        """Single word input."""
        input_str = "Single"
        expected = ["Single"]
        self.assertEqual(split_string(input_str), expected)

    def test_empty_string_input(self):
        """Empty string input."""
        input_str = ""
        expected = []
        self.assertEqual(split_string(input_str), expected)

    def test_leading_and_trailing_spaces(self):
        """String with leading and trailing spaces."""
        input_str = "   Leading and trailing spaces   "
        expected = ["Leading", "and", "trailing", "spaces"]
        self.assertEqual(split_string(input_str), expected)
