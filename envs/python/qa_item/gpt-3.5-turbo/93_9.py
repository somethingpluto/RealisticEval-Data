from typing import List


def get_all_alphabets() -> List[str]:
    """
    Produces a list of length 52 containing all lowercase and uppercase letters in alphabetical order.

    Returns:
        list[str]: A list of alphabet characters from 'a' to 'z' and 'A' to 'Z'.
    """
    alphabets = [chr(i) for i in range(65, 91)]  # Uppercase letters (A-Z)
    alphabets += [chr(i) for i in range(97, 123)]  # Lowercase letters (a-z)
    
    return alphabets
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