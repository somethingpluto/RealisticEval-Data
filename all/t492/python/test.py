import unittest


class TestFormatContent(unittest.TestCase):

    def test_extra_blank_lines(self):
        """ Test input with multiple blank lines. """
        input_text = "This is line 1.\n\n\nThis is line 2.\n\n\n\nThis is line 3."
        expected_output = "This is line 1.\n\nThis is line 2.\n\nThis is line 3."
        self.assertEqual(format_content(input_text), expected_output)

    def test_leading_and_trailing_spaces(self):
        """ Test input with leading and trailing spaces. """
        input_text = "   This is line 1.   \n\n   This is line 2.   "
        expected_output = "This is line 1.\n\nThis is line 2."
        self.assertEqual(format_content(input_text), expected_output)

    def test_multiple_spaces_between_words(self):
        """ Test input with multiple spaces between words. """
        input_text = "This  is   a    test. \n\nAnother    test    line."
        expected_output = "This is a test.\n\nAnother test line."
        self.assertEqual(format_content(input_text), expected_output)

    def test_only_blank_lines(self):
        """ Test input that contains only blank lines. """
        input_text = "\n\n\n\n"
        expected_output = ""
        self.assertEqual(format_content(input_text), expected_output)

    def test_empty_string(self):
        """ Test input that is an empty string. """
        input_text = ""
        expected_output = ""
        self.assertEqual(format_content(input_text), expected_output)