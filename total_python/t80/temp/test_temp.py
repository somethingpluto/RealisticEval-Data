import unittest


class TestSanitizeFilename(unittest.TestCase):
    def test_illegal_characters(self):
        self.assertEqual(sanitize_filename("filename<>:\"/\\|?*.txt"), "filename.txt")

    def test_multiple_spaces(self):
        self.assertEqual(sanitize_filename("my   document   name .txt "), "my document name.txt")

    def test_trailing_period(self):
        self.assertEqual(sanitize_filename("document. "), "document")

    def test_complex_example(self):
        self.assertEqual(sanitize_filename("  example?name*file<>.txt "), "example namefile.txt")

    def test_no_modifications_needed(self):
        self.assertEqual(sanitize_filename("valid_filename.txt"), "valid_filename.txt")
import re


def sanitize_filename(filename: str) -> str:
    """
    Sanitize a string to make it comply with Windows filename rules.

    Args:
    filename (str): The original filename string to be sanitized.

    Returns:
    str: A sanitized string that is safe to use as a Windows filename.
    """
    # Remove illegal characters
    illegal_chars = r'[<>:"/\\|?*]'
    filename = re.sub(illegal_chars, '', filename)

    # Replace multiple spaces with a single space
    filename = re.sub(r'\s+', ' ', filename).strip()

    # Remove trailing period if any (Windows filenames cannot end with a period)
    if filename.endswith('.'):
        filename = filename.rstrip('.')

    return filename
