def extract_outermost_brackets(s: str) -> str:
    """
    Extracts the contents of the outermost brackets from the input string.

    Args:
        s (str): The input string containing brackets.

    Returns:
        str: The contents within the outermost brackets, or an empty string if no brackets are found.
    """
    start_index = s.find('[')
    if start_index == -1:
        return ""
    
    end_index = -1
    bracket_count = 1
    for i in range(start_index + 1, len(s)):
        if s[i] == '[':
            bracket_count += 1
        elif s[i] == ']':
            bracket_count -= 1
            if bracket_count == 0:
                end_index = i
                break
    
    if end_index == -1:
        return ""
    
    return s[start_index + 1:end_index]
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