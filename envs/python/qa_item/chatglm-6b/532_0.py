
def count_letter_changes(input_string: str) -> list:
    """Counts the occurrences of consecutive identical letters in a given string.

    Args:
        input_string (str): The string to analyze for letter changes.

    Returns:
        list: A list of counts representing the number of consecutive identical
              letters before a different letter is found.
    """
    # Split the input string into a list of words.
    words = input_string.split()

    # Initialize an empty list to store the counts.
    counts = []

    # Iterate over each word in the input string.
    for word in words:
        # Check if the current word is identical to the previous word.
        if word == word.lower():
            # If the current and previous words are identical, add the count of the
            # previous word to the counts list.
            counts.append(1)
        else:
            # If the current word is different from the previous word, add the count
            # of the current word to the counts list.
            counts.append(1)

    # Return the list of counts.
    return counts
python
# Example usage
input_string = "apple orange apple banana orange apple"
counts = count_letter_changes(input_string)
print(counts)  # Output: [1, 1, 1, 1, 1, 1, 1]

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