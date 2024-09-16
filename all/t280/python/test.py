import unittest


class TestDedentText(unittest.TestCase):
    def test_uniform_indentation(self):
        """Test a string where all lines are uniformly indented."""
        text = """
                Line one
                Line two
                Line three
            """
        expected_result = """
Line one
Line two
Line three
"""
        result = dedent_text(text)
        self.assertEqual(result, expected_result)

    def test_mixed_indentation(self):
        """Test a string with mixed levels of indentation."""
        text = """
            Line one
                Line two
            Line three
        """
        expected_result = """
Line one
    Line two
Line three
"""
        result = dedent_text(text)
        self.assertEqual(result, expected_result)

    def test_no_indentation(self):
        """Test a string with no indentation at all."""
        text = """
Line one
Line two
Line three
"""
        expected_result = """
Line one
Line two
Line three
"""
        result = dedent_text(text)
        self.assertEqual(result, expected_result)

    def test_including_tabs(self):
        """Test a string that includes tab characters as indentation."""
        text = "\t\tLine one\n\t\t\tLine two\n\t\tLine three\n"
        expected_result = "Line one\n\tLine two\nLine three\n"
        result = dedent_text(
            text.replace('\t', '    '))  # Convert tabs to spaces assuming a tab is equivalent to four spaces
        self.assertEqual(result, expected_result)

    def test_empty_string(self):
        """Test an empty string."""
        text = ""
        expected_result = ""
        result = dedent_text(text)
        self.assertEqual(result, expected_result)
