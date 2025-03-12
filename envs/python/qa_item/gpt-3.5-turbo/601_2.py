from typing import List, Set, Dict, Tuple, Optional

def count_words(s: str) -> int:
    words = s.split()
    return len(words)
import unittest


class TestWordCount(unittest.TestCase):
    def test_count_words(self):
        # Test cases for count_words
        self.assertEqual(tester.count_words(""), 0)  # Empty string
        self.assertEqual(tester.count_words("     "), 0)  # String with only spaces
        self.assertEqual(tester.count_words("Hello"), 1)  # Single word
        self.assertEqual(tester.count_words("This is a test string"), 5)  # Multiple words with single spaces
        self.assertEqual(tester.count_words("This    is   a   test   string"), 5)  # Multiple spaces between words
        self.assertEqual(tester.count_words("   Hello world!   "), 2)  # Leading and trailing spaces

if __name__ == '__main__':
    unittest.main()