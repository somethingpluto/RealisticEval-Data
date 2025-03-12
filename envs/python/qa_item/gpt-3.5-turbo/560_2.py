import re

def get_line_number(content: str, index: int) -> int:
    pattern = re.compile(r'\n')
    lines = pattern.split(content)
    
    line_number = 1
    character_count = 0
    
    for line in lines:
        character_count += len(line) + 1
        if character_count > index:
            break
        line_number += 1
    
    return line_number
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