def is_significant_number(input_value: str) -> bool:
    """
    Check if the given input is a significant number.

    A significant number is defined as a string that:
    - Has a length between 5 and 18 characters (inclusive).
    - Contains only digit characters.
    - Cannot start with '0' if its length is greater than 1.
    Args:
        input_value (str): The input value to be checked.

    Returns:
        bool: True if the input is a significant number, False otherwise.
    """
    
    if len(input_value) < 5 or len(input_value) > 18:
        return False
    
    if not input_value.isdigit():
        return False
    
    if len(input_value) > 1 and input_value[0] == '0':
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