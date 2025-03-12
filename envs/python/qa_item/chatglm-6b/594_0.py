
from typing import List

def split_comma(s: str) -> List[str]:
    """
    Splits a comma-separated string into individual tokens.
    This function takes a string containing comma-separated values, trims
    leading and trailing whitespace from each token, and stores the non-empty
    tokens in the provided list.

    Args:
        s (str): The input string to be split, which may contain leading and trailing whitespace around the tokens.

    Returns:
        List[str]: A list where the resulting tokens will be stored. The list will be cleared before storing the new tokens.
    """
    # Clear the input string before splitting
    input_str = input_str.strip()
    # Split the input string into tokens
    tokens = input_str.split(",")
    # Trim leading and trailing whitespace from each token
    tokens = [token.strip() for token in tokens]
    # Return the resulting list of tokens
    return tokens
python
# Example usage
result = split_comma("Hello, world!")
print(result)  # Output: ["Hello", "world!"]

import unittest


class Tester(unittest.TestCase):

    def test_basic_comma_separated_values(self):
        result = split_comma("apple,banana,orange")
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], "apple")
        self.assertEqual(result[1], "banana")
        self.assertEqual(result[2], "orange")

    def test_leading_and_trailing_whitespace(self):
        result = split_comma("  apple , banana , orange  ")
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], "apple")
        self.assertEqual(result[1], "banana")
        self.assertEqual(result[2], "orange")

    def test_multiple_consecutive_commas(self):
        result = split_comma("apple,,banana,,,orange")
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], "apple")
        self.assertEqual(result[1], "banana")
        self.assertEqual(result[2], "orange")

    def test_empty_input_string(self):
        result = split_comma("")
        self.assertEqual(len(result), 0)

    def test_only_whitespace_input(self):
        result = split_comma("   ")
        self.assertEqual(len(result), 0)

    def test_trailing_commas(self):
        result = split_comma("apple,banana,orange,")
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], "apple")
        self.assertEqual(result[1], "banana")
        self.assertEqual(result[2], "orange")

if __name__ == '__main__':
    unittest.main()