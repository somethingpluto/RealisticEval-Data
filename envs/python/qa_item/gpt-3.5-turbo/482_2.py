def extract_outermost_brackets(s: str) -> str:
    opening_bracket = -1
    closing_bracket = -1
    
    for i in range(len(s)):
        if s[i] == "[":
            opening_bracket = i
        elif s[i] == "]" and opening_bracket != -1:
            closing_bracket = i
            break
    
    if opening_bracket != -1 and closing_bracket != -1:
        return s[opening_bracket+1:closing_bracket]
    else:
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