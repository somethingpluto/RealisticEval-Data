
import re

def remove_inner_asterisks(text: str) -> str:
    patterns = re.compile(r'(*\w+)')  # create a regular expression pattern to match '(*...*)'
    for pattern in patterns.findall(text):
        # remove any asterisks inside the parentheses while preserving the outer format
        text = text.replace(pattern, '')
        # add the parentheses to the end of the text to match the original format
        text = text.replace(pattern, '(' + pattern + ')')
        # return the modified text
        return text

import unittest
import re


class TestTransformParentheses(unittest.TestCase):

    def test_basic_case(self):
        text = "Hello (*wo*rld*)!"
        expected = "Hello (*world*)!"
        self.assertEqual(remove_inner_asterisks(text), expected)

    def test_multiple_asterisks(self):
        text = "(*he*l*lo*)"
        expected = "(*hello*)"
        self.assertEqual(remove_inner_asterisks(text), expected)

    def test_no_asterisks_inside(self):
        text = "(*hello*)"
        expected = "(*hello*)"
        self.assertEqual(remove_inner_asterisks(text), expected)

    def test_multiple_patterns(self):
        text = "(*hi*), (*there*), (*world*)!"
        expected = "(*hi*), (*there*), (*world*)!"
        self.assertEqual(remove_inner_asterisks(text), expected)

    def test_no_matching_pattern(self):
        text = "This is a test without matching parentheses."
        expected = "This is a test without matching parentheses."
        self.assertEqual(remove_inner_asterisks(text), expected)

if __name__ == '__main__':
    unittest.main()