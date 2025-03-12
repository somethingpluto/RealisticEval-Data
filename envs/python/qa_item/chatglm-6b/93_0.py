
from typing import List

def get_all_alphabets() -> List[str]:
    """
    Produces a list of length 52 containing all lowercase and uppercase letters in alphabetical order.

    Returns:
        List[str]: A list of alphabet characters from 'a' to 'z' and 'A' to 'Z'.
    """
    # Initialize the list to contain all lowercase letters
    lower_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # Initialize the list to contain all uppercase letters
    upper_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # Iterate over the lowercase and uppercase alphabets
    for letter in lower_alphabet:
        # If the current letter is not in the uppercase alphabet, add it to the list
        if letter not in upper_alphabet:
            upper_alphabet.append(letter)

    # Return the list of all uppercase and lowercase letters
    return upper_alphabet + lower_alphabet

import unittest


class TestGetAllAlphabets(unittest.TestCase):

    def test_return_length(self):
        result = get_all_alphabets()
        self.assertEqual(len(result), 52)

    def test_lowercase_alphabets(self):
        result = get_all_alphabets()
        lowercase_alphabets = result[:26]
        self.assertEqual(lowercase_alphabets, [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ])

    def test_uppercase_alphabets(self):
        result = get_all_alphabets()
        uppercase_alphabets = result[26:]
        self.assertEqual(uppercase_alphabets, [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ])

    def test_first_element(self):
        result = get_all_alphabets()
        self.assertEqual(result[0], 'a')

    def test_last_element(self):
        result = get_all_alphabets()
        self.assertEqual(result[-1], 'Z')

if __name__ == '__main__':
    unittest.main()