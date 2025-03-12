def extract_outermost_brackets(s: str) -> str:
    stack = []
    start = -1
    end = -1
    
    for i in range(len(s)):
        if s[i] == '[':
            stack.append(i)
        elif s[i] == ']' and stack:
            start = stack.pop()
            end = i
            break
    
    if start != -1 and end != -1:
        return s[start+1:end]
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