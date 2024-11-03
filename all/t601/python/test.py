import unittest



class TestWordCount(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(count_words(""), 0)  # Empty string

    def test_spaces_only(self):
        self.assertEqual(count_words("     "), 0)  # String with only spaces

    def test_single_word(self):
        self.assertEqual(count_words("Hello"), 1)  # Single word

    def test_multiple_words_single_spaces(self):
        self.assertEqual(count_words("This is a test string"), 5)  # Multiple words with single spaces

    def test_multiple_spaces_between_words(self):
        self.assertEqual(count_words("This    is   a   test   string"), 5)  # Multiple spaces between words

    def test_leading_trailing_spaces(self):
        self.assertEqual(count_words("   Hello world!   "), 2)  # Leading and trailing spaces