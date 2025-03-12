\s*?\n(.*?)\n
import unittest


class TestFormatStr(unittest.TestCase):

    def test_simple_string(self):
        """Test a simple string input."""
        input_str = "Hello, World!"
        expected_output = "> Hello, World!"
        self.assertEqual(format_str_2_markdown(input_str), expected_output)

    def test_multiline_string(self):
        """Test a multiline string input."""
        input_str = "Line 1\nLine 2\nLine 3"
        expected_output = "> Line 1\n> Line 2\n> Line 3"
        self.assertEqual(format_str_2_markdown(input_str), expected_output)

    def test_code_block_delimiters_even(self):
        """Test a string with an even number of code block delimiters."""
        input_str = "Some code:\n```\nprint('Hello')\n```"
        expected_output = "> Some code:\n> ```\n> print('Hello')\n> ```"
        self.assertEqual(format_str_2_markdown(input_str), expected_output)

    def test_code_block_delimiters_odd(self):
        """Test a string with an odd number of code block delimiters."""
        input_str = "Some code:\n```\nprint('Hello')"
        expected_output = "> Some code:\n> ```\n> print('Hello')\n> ```"
        self.assertEqual(format_str_2_markdown(input_str), expected_output)

    def test_non_string_input(self):
        """Test non-string input (e.g., integer) to ensure it's converted."""
        input_value = 123
        expected_output = "> 123"
        self.assertEqual(format_str_2_markdown(input_value), expected_output)
if __name__ == '__main__':
    unittest.main()