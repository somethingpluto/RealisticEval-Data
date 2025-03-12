
def compress_whitespace(input_string: str) -> str:
    # Find all consecutive whitespace characters in the input string
     consecutive_whitespace = []
    for char in input_string:
        if char.isspace():
             consecutive_whitespace.append(char)
    
    # Replace all consecutive whitespace characters with a single space
    output_string = " ".join( consecutive_whitespace)
    return output_string

import unittest


class TestCompressWhitespace(unittest.TestCase):

    def test_single_spaces(self):
        """Test with a string containing single spaces"""
        self.assertEqual(compress_whitespace("This is a test string."), "This is a test string.")

    def test_multiple_spaces(self):
        """Test with a string containing multiple spaces"""
        self.assertEqual(compress_whitespace("This    is  a   test   string."), "This is a test string.")

    def test_leading_trailing_spaces(self):
        """Test with leading and trailing spaces"""
        self.assertEqual(compress_whitespace("   Leading and trailing spaces   "), "Leading and trailing spaces")

    def test_only_spaces(self):
        """Test with a string containing only spaces"""
        self.assertEqual(compress_whitespace("       "), "")

    def test_empty_string(self):
        """Test with an empty string"""
        self.assertEqual(compress_whitespace(""), "")
if __name__ == '__main__':
    unittest.main()