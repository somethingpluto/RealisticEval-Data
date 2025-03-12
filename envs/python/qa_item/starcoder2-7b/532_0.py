def count_letter_changes(input_string: str) -> list:
    counts = []
    count = 1
    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i-1]:
            count += 1
        else:
            counts.append(count)
            count = 1
    counts.append(count)  # append the last count
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