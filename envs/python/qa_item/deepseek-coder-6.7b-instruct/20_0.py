import re

def remove_inner_asterisks(text: str) -> str:
    """
    Transforms the input text by finding and modifying patterns that match the format '(*...*)'.
    Specifically, it removes any asterisks inside the parentheses while preserving the outer format.

    Args:
        text (str): The input text containing patterns to be transformed.

    Returns:
        str: The transformed text with asterisks inside '(*...*)' patterns removed.
    """
    # Define the regex pattern to match the format '(*...*)'
    pattern = r'\*(.*?)\*'
    
    # Function to remove asterisks inside the matched pattern
    def remove_asterisks(match):
        return '*' + match.group(1).replace('*', '') + '*'
    
    # Apply the regex substitution
    result = re.sub(pattern, remove_asterisks, text)
    
    return result
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