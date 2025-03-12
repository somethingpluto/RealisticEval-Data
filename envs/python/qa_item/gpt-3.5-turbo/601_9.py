def count_words(s: str) -> int:
    """
    Count the number of words in a given string.

    A word is defined as a sequence of characters separated by whitespace.
    This function handles leading and trailing whitespace, as well as
    multiple spaces between words.

    Args:
        s (str): The input string in which words are to be counted.

    Returns:
        int: The count of words in the input string.
    """
    if not s:
        return 0
    
    count = 0
    in_word = False
    
    for char in s:
        if char.isspace():
            if in_word:
                count += 1
                in_word = False
        else:
            in_word = True
    
    if in_word:
        count += 1
    
    return count
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