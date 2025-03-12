def count_letter_changes(input_string: str) -> list:
    count_list = []
    current_char = input_string[0]
    current_count = 1

    for char in input_string[1:]:
        if char == current_char:
            current_count += 1
        else:
            count_list.append(current_count)
            current_char = char
            current_count = 1

    # Add the last count to the list
    count_list.append(current_count)

    return count_list
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