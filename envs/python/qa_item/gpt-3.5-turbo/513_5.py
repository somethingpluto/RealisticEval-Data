import re

def is_phrase_in_string_ignore_case(phrase: str, string: str) -> bool:
    clean_phrase = re.sub(r'\s+', ' ', phrase.lower().strip())
    clean_string = re.sub(r'\s+', ' ', string.lower().strip())
    
    return re.search(r'\b' + re.escape(clean_phrase) + r'\b', clean_string) is not None
import unittest


class TestIsPhraseInStringIgnoreCase(unittest.TestCase):

    def test_exact_match_case_insensitive(self):
        self.assertTrue(is_phrase_in_string_ignore_case("hello world", "Hello World"))


    def test_partial_word_match_case_insensitive(self):
        self.assertTrue(is_phrase_in_string_ignore_case("Hello", "saying Hello there"))

    def test_different_cases(self):
        self.assertTrue(is_phrase_in_string_ignore_case("HELLO", "hello there!"))
        self.assertTrue(is_phrase_in_string_ignore_case("world", "WORLD is great"))

    def test_non_existent_phrase(self):
        self.assertFalse(is_phrase_in_string_ignore_case("goodbye", "Hello world"))
        self.assertFalse(is_phrase_in_string_ignore_case("hello", "goodbye world"))


if __name__ == '__main__':
    unittest.main()