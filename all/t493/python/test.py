import unittest


class TestWrapContentGenerator(unittest.TestCase):
    def test_long_line(self):
        """Test a single long line that exceeds the specified width."""
        content = "This is a very long line that needs to be wrapped according to the specified width."
        expected_output = [
            "This is a very long line that needs to be wrapped according to the specified width."
        ]
        self.assertEqual(list(wrap_content_generator(content, width=50)), expected_output)

    def test_multiple_lines(self):
        """Test multiple lines of varying lengths."""
        content = "First line.\nSecond line is a bit longer than the first.\nShort."
        expected_output = [
            "First line.\n",
            "Second line is a bit longer than the\nfirst.\n",
            "Short."
        ]
        self.assertEqual(list(wrap_content_generator(content, width=30)), expected_output)

    def test_empty_lines(self):
        """Test content with empty lines to ensure they are preserved."""
        content = "Line one.\n\nLine three.\n"
        expected_output = [
            "Line one.\n",
            "\n",
            "Line three.\n"
        ]
        self.assertEqual(list(wrap_content_generator(content, width=50)), expected_output)

    def test_exact_width(self):
        """Test a line that is exactly the specified width."""
        content = "A line that is exactly eighty characters long and should not be wrapped."
        expected_output = [
            "A line that is exactly eighty characters long and should not be wrapped."
        ]
        self.assertEqual(list(wrap_content_generator(content, width=80)), expected_output)

    def test_different_widths(self):
        """Test the function with different widths to verify wrapping behavior."""
        content = "This is a test sentence that will be wrapped differently based on width."
        expected_output_30 = [
            "This is a test sentence that will be\nwrapped differently based on width."
        ]
        expected_output_20 = [
            "This is a test\nsentence that\nwill be\nwrapped\ndifferently\nbased on\nwidth."
        ]
        self.assertEqual(list(wrap_content_generator(content, width=30)), expected_output_30)
        self.assertEqual(list(wrap_content_generator(content, width=20)), expected_output_20)
