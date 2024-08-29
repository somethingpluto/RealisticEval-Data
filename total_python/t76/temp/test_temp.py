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
        input_text = "    Line one\n  Line two\n    Line three"
        expected_output = "  Line one\nLine two\n  Line three"
        self.assertEqual(remove_common_indentation(input_text), expected_output, "Should remove the minimum common indentation")

    def test_lines_with_only_whitespace(self):
        # Testing lines that contain only whitespace characters
        input_text = "    \n    \n  \n"
        expected_output = "    \n    \n  \n"
        self.assertEqual(remove_common_indentation(input_text), expected_output, "Should handle lines with only whitespace correctly")


def remove_common_indentation(multiline_text: str) -> str:
    """
    Removes the common leading indentation from each line in a given multi-line string,
    preserving the relative indentation of the text.

    Args:
        multiline_text (str): The input string containing multiple lines.

    Returns:
        str: The sanitized string with common leading indentation removed.
    """
    lines = multiline_text.split('\n')

    # Filter out lines that are empty or only whitespace, as they do not affect minimum indentation
    non_empty_lines = [line for line in lines if line.strip() != '']

    # Determine the minimum indentation of non-empty lines
    min_indent = float('inf')
    for line in non_empty_lines:
        stripped_line = line.lstrip()
        indent = len(line) - len(stripped_line)
        min_indent = min(min_indent, indent)

    # If there's no indentation or all lines are empty, return the original string
    if min_indent == float('inf'):
        return multiline_text

    # Remove the common leading indentation from each line
    sanitized_lines = [line[min_indent:] for line in lines]

    return '\n'.join(sanitized_lines)
