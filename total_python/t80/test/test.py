import unittest


class TestSanitizeFilename(unittest.TestCase):
    def test_remove_illegal_chars(self):
        # Test removing characters illegal in Windows filenames
        result = sanitize_filename("test.js<filename>?*.txt")
        self.assertEqual(result, "testfilename.txt")

    def test_replace_multiple_spaces(self):
        # Test replacing multiple spaces with a single space
        result = sanitize_filename("new  document   file.txt")
        self.assertEqual(result, "new document file.txt")

    def test_remove_trailing_periods(self):
        # Test removing trailing periods
        result = sanitize_filename("example.")
        self.assertEqual(result, "example")

    def test_complex_filename(self):
        # Test a complex filename with multiple issues
        result = sanitize_filename("  test.js*file<>name  with  ?illegal|chars.txt  ")
        self.assertEqual(result, "testfilename with illegalchars.txt")

    def test_empty_filename(self):
        # Test sanitizing an empty filename
        result = sanitize_filename("")
        self.assertEqual(result, "")
