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