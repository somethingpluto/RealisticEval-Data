def extract_outermost_brackets(s: str) -> str:
    stack = []
    start = -1
    
    for i, char in enumerate(s):
        if char == '[':
            if not stack:
                start = i + 1
            stack.append(char)
        elif char == ']' and stack:
            stack.pop()
            if not stack:
                return s[start:i]
    
    return ""
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