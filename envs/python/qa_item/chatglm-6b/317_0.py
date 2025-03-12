
def count_letters(s: str) -> int:
    """Count the number of letters in a string.

    Args:
        s (str): The input string from which to count letters.

    Returns:
        int: The count of letters in the string.
    """
    # Convert the string to lowercase
    s = s.lower()
    # Count the number of occurrences of each letter
    count = 0
    for c in s:
        count += 1
    # Return the count of letters
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
if __name__ == '__main__':
    unittest.main()