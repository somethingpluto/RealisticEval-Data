import string

def count_letters(s: str) -> int:
    """Count the number of letters in a string.

    Args:
        s (str): The input string from which to count letters.

    Returns:
        int: The count of letters in the string.
    """
    count = 0
    for char in s:
        if char.isalpha():
            count += 1
    return count
import unittest


class TestCountLetters(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(count_letters("Hello, World!"), 10)

    def test_no_letters(self):
        self.assertEqual(count_letters("12345"), 0)

    def test_abc_123_xyz(self):
        self.assertEqual(count_letters("abc 123 xyz!"), 6)

    def test_empty_string(self):
        self.assertEqual(count_letters(""), 0)

    def test_A1B2C3(self):
        self.assertEqual(count_letters("A1B2C3!@#"), 3)

    def test_mixed_case(self):
        self.assertEqual(count_letters("AbCdE"), 5)

    def test_special_characters(self):
        self.assertEqual(count_letters("Hello@2024!"), 10)

if __name__ == '__main__':
    unittest.main()