from typing import List

def compress_string(input: str, max_length: int = 18) -> str:
    """
    Compresses a string to ensure its length does not exceed the specified maximum length.
    If the string exceeds the maximum length, it truncates the string and appends an ellipsis ("...").

    Args:
        input (str): The string to be compressed.
        max_length (int, optional): The maximum allowed length of the string (default is 18).

    Returns:
        str: A compressed string that does not exceed the specified length.
             If truncation occurs, an ellipsis ("...") is appended.
    """

    if len(input) <= max_length:
        return input
    else:
        return input[:max_length-3] + "..."
import unittest


class TestCompressString(unittest.TestCase):
    def test_short_string(self):
        """ should return the original string if it is shorter than the max length """
        input_str = "Short string"
        result = compress_string(input_str)
        self.assertEqual(result, input_str)

    def test_exact_length_string(self):
        """ should return the original string if it is exactly equal to the max length """
        input_str = "Exactly 18 chars"
        result = compress_string(input_str)
        self.assertEqual(result, input_str)

    def test_truncate_long_string(self):
        """ should truncate the string and append "..." if it exceeds the max length """
        input_str = "This is a long string that needs to be compressed."
        result = compress_string(input_str)
        self.assertEqual(result, "This is a long ...")

    def test_truncate_with_custom_max_length(self):
        """ should truncate the string to maxLength - 3 and append "..." when maxLength is specified """
        input_str = "Another long string that is definitely too long."
        result = compress_string(input_str, 25)
        self.assertEqual(result, "Another long string th...")

    def test_default_max_length(self):
        """ should use default max length of 18 if no maxLength is provided """
        input_str = "This string is way too long."
        result = compress_string(input_str)
        self.assertEqual(result, "This string is ...")

    def test_empty_string(self):
        """ should return the original string if it is empty """
        input_str = ""
        result = compress_string(input_str)
        self.assertEqual(result, input_str)

if __name__ == '__main__':
    unittest.main()