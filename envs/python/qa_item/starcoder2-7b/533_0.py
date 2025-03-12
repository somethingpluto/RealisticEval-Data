import random

def shuffle_string(input_string: str) -> str:
    """Shuffles the characters in a given string randomly.

    Args:
        input_string (str): The string to shuffle.

    Returns:
        str: A new string with the characters shuffled.
    """
    # Convert the input string to a list of characters
    char_list = list(input_string)
    
    # Shuffle the list of characters
    random.shuffle(char_list)
    
    # Join the shuffled characters back into a string
    shuffled_string = ''.join(char_list)
    
    return shuffled_string
import unittest


class TestShuffleString(unittest.TestCase):

    def test_same_length(self):
        input_string = "abcdef"
        result = shuffle_string(input_string)
        self.assertEqual(len(result), len(input_string))

    def test_shuffle_characters(self):
        input_string = "hello"
        result = shuffle_string(input_string)
        self.assertNotEqual(result, input_string)  # It should be different most of the time

    def test_empty_string(self):
        input_string = ""
        result = shuffle_string(input_string)
        self.assertEqual(result, "")  # Should return an empty string

    def test_single_character(self):
        input_string = "a"
        result = shuffle_string(input_string)
        self.assertEqual(result, "a")  # Should return the same single character

    def test_identical_characters(self):
        input_string = "aaaaa"
        result = shuffle_string(input_string)
        self.assertEqual(result, "aaaaa")  # Should return the same string

    def test_long_string(self):
        input_string = "abcdefghijklmnopqrstuvwxyz"
        result = shuffle_string(input_string)
        self.assertNotEqual(result, input_string)  # It should be different most of the time
        self.assertEqual(len(result), len(input_string))  # Length should be the same

    def test_same_string_characters(self):
        input_string = "111111"
        result = shuffle_string(input_string)
        self.assertEqual(result, "111111")  # Should return the same string

    def test_special_characters(self):
        input_string = "a!@#$%^&*()_+"
        result = shuffle_string(input_string)
        self.assertEqual(len(result), len(input_string))  # Length should be the same
        self.assertNotEqual(result, input_string)  # It should be different most of the time

if __name__ == '__main__':
    unittest.main()