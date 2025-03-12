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
    # Split the string by commas
    tokens = s.split(',')
    
    # Trim whitespace from each token and filter out empty tokens
    tokens = [token.strip() for token in tokens if token.strip()]
    
    return tokens
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