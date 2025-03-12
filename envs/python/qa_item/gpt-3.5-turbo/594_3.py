from typing import List

def split_comma(s: str) -> List[str]:
    tokens = [token.strip() for token in s.split(",") if token.strip()]
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