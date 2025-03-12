import re

def remove_inner_asterisks(text: str) -> str:
    pattern = r'\((.*?)\)'
    matches = re.findall(pattern, text)
    
    for match in matches:
        new_match = match.replace('*', '')
        text = text.replace(f'({match})', f'({new_match})')
    
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