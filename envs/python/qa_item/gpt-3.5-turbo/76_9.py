import re

def remove_common_indentation(multiline_text: str) -> str:
    lines = multiline_text.split('\n')
    lines = [line.lstrip() for line in lines]
    
    min_indent = float('inf')
    for line in lines:
        if line.strip():
            min_indent = min(min_indent, len(re.match(r'^\s*', line).group()))
    
    sanitized_text = ''
    for line in lines:
        if line.strip():
            sanitized_text += line[min_indent:] + '\n'
        else:
            sanitized_text += '\n'
    
    return sanitized_text
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