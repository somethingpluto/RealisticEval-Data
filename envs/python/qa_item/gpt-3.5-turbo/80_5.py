import re

def sanitize_filename(filename: str) -> str:
    """
    remove illegal characters from windows file path string

    Args:
        filename (str): The original filename string to be sanitized.

    Returns:
        str: A sanitized string that is safe to use as a Windows filename.
    """
    illegal_chars = '<>:"/\|?*'
    sanitized_filename = re.sub(r'[{}]'.format(re.escape(illegal_chars)), '', filename)
    
    return sanitized_filename
import unittest


class TestSanitizeFilename(unittest.TestCase):

    def test_valid_filename(self):
        self.assertEqual(sanitize_filename("valid_filename.txt"), "valid_filename.txt")

    def test_illegal_characters(self):
        self.assertEqual(sanitize_filename("invalid<filename>.txt"), "invalid_filename_.txt")
        self.assertEqual(sanitize_filename("file/name:with*illegal|chars?.txt"), "file_name_with_illegal_chars_.txt")


    def test_long_filename(self):
        long_filename = "a" * 300 + ".txt"
        sanitized_filename = sanitize_filename(long_filename)
        self.assertEqual(len(sanitized_filename), 255)
        self.assertEqual(sanitized_filename, "a" * 255)

    def test_empty_filename(self):
        self.assertEqual(sanitize_filename(""), "")
if __name__ == '__main__':
    unittest.main()