def is_significant_number(input_value: str) -> bool:
    if not (5 <= len(input_value) <= 18):
        return False

    if input_value[0] == '0' and len(input_value) > 1:
        return False

    for char in input_value:
        if not char.isdigit():
            return False

    return True
import unittest


class TestIsSignificantNumber(unittest.TestCase):

    def test_valid_significant_number_with_exactly_5_digits(self):
        self.assertTrue(is_significant_number("12345"))

    def test_number_with_leading_zero(self):
        self.assertFalse(is_significant_number("01234"))

    def test_valid_significant_number_with_exactly_18_digits(self):
        self.assertTrue(is_significant_number("123456789012345678"))

    def test_number_with_less_than_5_digits(self):
        self.assertFalse(is_significant_number("123"))

    def test_number_with_more_than_18_digits(self):
        self.assertFalse(is_significant_number("1234567890123456789"))

    def test_number_containing_non_digit_characters(self):
        self.assertFalse(is_significant_number("1234a"))

    def test_single_zero(self):
        self.assertFalse(is_significant_number("0"))

    def test_non_string_input(self):
        self.assertFalse(is_significant_number(12345))

if __name__ == '__main__':
    unittest.main()