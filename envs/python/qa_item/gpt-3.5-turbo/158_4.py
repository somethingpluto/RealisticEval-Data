import os

def get_file_extension(file_name: str) -> str:
    """
    Extract the file extension and return it if it exists. If not, an empty string is returned.

    Args:
        file_name (str): The full name of the file from which to extract the extension.

    Returns:
        str: The file extension without the dot, or an empty string if no extension is found.
    """
    return os.path.splitext(file_name)[1].lstrip('.') if '.' in file_name else ''
import unittest


class TestGetFileExtension(unittest.TestCase):

    def test_standard_file_extension(self):
        """should return the file extension for a standard file"""
        self.assertEqual(get_file_extension('example.txt'), 'txt')

    def test_no_extension(self):
        """should return an empty string for files without an extension"""
        self.assertEqual(get_file_extension('example'), '')

    def test_multiple_dots(self):
        """should handle files with multiple dots"""
        self.assertEqual(get_file_extension('example.with.many.dots.jpg'), 'jpg')

    def test_filenames_ending_with_dot(self):
        """should return an empty string for filenames that end with a dot"""
        self.assertEqual(get_file_extension('example.'), '')

    def test_case_sensitivity(self):
        """should correctly handle case sensitivity"""
        self.assertEqual(get_file_extension('example.JPG'), 'JPG')

if __name__ == '__main__':
    unittest.main()