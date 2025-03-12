
def extract_outermost_brackets(s: str) -> str:
    """
    Extracts the contents of the outermost brackets from the input string.
    For example:
        input: Text [with [nested] brackets] and more text
        output: with [nested] brackets
    Args:
        s (str): The input string containing brackets.

    Returns:
        str: The contents within the outermost brackets, or an empty string if no brackets are found.
    """
     brackets = s.strip().split("[")[1].strip()
    return brackets if brackets else ""

import unittest


class TestExtractOutermostBrackets(unittest.TestCase):
    
    def test_single_parentheses(self):
        self.assertEqual(extract_outermost_brackets("Text (example) more text"), "example")

    def test_nested_brackets(self):
        self.assertEqual(extract_outermost_brackets("Text {with some {nested} brackets}"), "with some {nested} brackets")

    def test_square_brackets(self):
        self.assertEqual(extract_outermost_brackets("Text [with [nested] brackets] and more text"), "with [nested] brackets")

    def test_mixed_bracket_types(self):
        self.assertEqual(extract_outermost_brackets("Mixed (types {of brackets [in use]})"), "types {of brackets [in use]}")

    def test_no_brackets(self):
        self.assertEqual(extract_outermost_brackets("No brackets here"), "")
if __name__ == '__main__':
    unittest.main()