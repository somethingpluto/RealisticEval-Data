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

def dedent_text(text):
    """
    Removes excess indentation from a multiline string while preserving the relative indentation levels.

    Args:
    text (str): The multiline string to dedent.

    Returns:
    str: The dedented multiline string.
    """
    # Split the text into lines
    lines = text.splitlines()

    # Filter out blank lines for the purpose of finding the minimum indentation
    non_blank_lines = [line for line in lines if line.strip()]

    # Find the minimum indentation (excluding lines that are blank)
    min_indent = min((len(line) - len(line.lstrip()) for line in non_blank_lines), default=0)

    # Remove the minimum indentation from all lines
    dedented_lines = [line[min_indent:] if len(line) >= min_indent else line for line in lines]

    # Join the lines back into a single string with corrected indentation
    dedented_text = '\n'.join(dedented_lines)

    return dedented_text