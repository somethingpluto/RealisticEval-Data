def count_letter_changes(input_string: str) -> list:
    """
    Counts the occurrences of consecutive identical letters in a given string.

    Args:
        input_string (str): The string to analyze for letter changes.

    Returns:
        list: A list of counts representing the number of consecutive
              identical letters before a different letter is found.
    """
    if not input_string:
        return []

    counts = []
    current_char = input_string[0]
    current_count = 0

    for char in input_string:
        if char == current_char:
            current_count += 1
        else:
            counts.append(current_count)
            current_char = char
            current_count = 1
    counts.append(current_count)

    return counts
import unittest


class TestCountLetterChanges(unittest.TestCase):

    def test_count_consecutive_letters_correctly(self):
        result = count_letter_changes("aaabbcdeee")
        self.assertEqual(result, [3, 2, 1, 1, 3])

    def test_single_character_count(self):
        result = count_letter_changes("a")
        self.assertEqual(result, [1])

    def test_no_consecutive_letters(self):
        result = count_letter_changes("abcdef")
        self.assertEqual(result, [1, 1, 1, 1, 1, 1])

    def test_identical_letters(self):
        result = count_letter_changes("rrrrrr")
        self.assertEqual(result, [6])

    def test_long_string_random_letters(self):
        result = count_letter_changes("xxxyyyzzzaaaab")
        self.assertEqual(result, [3, 3, 3, 4, 1])

    def test_numeric_characters(self):
        result = count_letter_changes("1122334455")
        self.assertEqual(result, [2, 2, 2, 2, 2])

if __name__ == '__main__':
    unittest.main()