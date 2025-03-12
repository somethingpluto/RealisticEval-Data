
def remove_common_indentation(multiline_text: str) -> str:
    """
    Removes the common leading indentation from each line in a given multi-line string,
    preserving the relative indentation of the text.

    Args:
        multiline_text (str): The input string containing multiple lines.

    Returns:
        str: The sanitized string with common leading indentation removed.
    """
    lines = multiline_text.split("\n")  # split the input string into a list of lines
    lines = [line.strip() for line in lines]  # remove trailing whitespace from each line
    lines = [line.strip() for line in lines if line.strip()]  # remove leading whitespace
    return "\n".join(lines)  # join the lines back into a single string with newline characters

import unittest

class TestRemoveCommonIndentation(unittest.TestCase):

    def test_empty_string(self):
        # Testing edge case with an empty string
        self.assertEqual(remove_common_indentation(""), "", "Should return an empty string")

    def test_single_line_string(self):
        # Testing a single line with no indentation
        self.assertEqual(remove_common_indentation("No indentation here"), "No indentation here", "Should return the same string as input")

    def test_multiple_lines_with_uniform_indentation(self):
        # Testing basic logic with uniform indentation across multiple lines
        input_text = "    Line one\n    Line two\n    Line three"
        expected_output = "Line one\nLine two\nLine three"
        self.assertEqual(remove_common_indentation(input_text), expected_output, "Should remove common leading indentation")

    def test_multiple_lines_with_mixed_indentation(self):
        # Testing lines with mixed indentation levels
        input_text = "  Line one\n  Line two\n  Line three"
        expected_output = "Line one\nLine two\nLine three"
        self.assertEqual(remove_common_indentation(input_text), expected_output, "Should remove the minimum common indentation")


if __name__ == '__main__':
    unittest.main()