import re

def get_line_number(content: str, index: int) -> int:
    """
    Gets the line number in the content at the specified index.

    Args:
        content (str): The string content to check.
        index (int): The character index to find the line number for.

    Returns:
        int: The line number corresponding to the given index.
    """
    
    line_num = 1
    for match in re.finditer(r'\n', content):
        if match.start() <= index:
            line_num += 1
        else:
            break
    
    return line_num
import unittest


class TestGetLineNumber(unittest.TestCase):

    def test_returns_1_for_first_character(self):
        self.assertEqual(get_line_number("Line 1\nLine 2\nLine 3", 0), 1)

    def test_returns_1_for_last_character_of_first_line(self):
        self.assertEqual(get_line_number("Line 1\nLine 2\nLine 3", 5), 1)

    def test_returns_3_for_last_character_of_third_line(self):
        self.assertEqual(get_line_number("Line 1\nLine 2\nLine 3", 18), 3)

    def test_returns_1_for_single_line_string(self):
        self.assertEqual(get_line_number("Single line string", 0), 1)

    def test_returns_3_for_index_in_multiline_string_with_trailing_newlines(self):
        self.assertEqual(get_line_number("Line 1\nLine 2\nLine 3\n\n", 15), 3)

if __name__ == '__main__':
    unittest.main()