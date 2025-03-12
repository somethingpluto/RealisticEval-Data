import re

def is_have_phone_number(s: str) -> bool:
    """
    Determines whether the string contains a phone number; a possible format for a phone number is +1-800-555-1234, 555-555-1234, 555 555 1234.

    Args:
        s (str): Input string that may contain a phone number.

    Returns:
        bool: True if the string contains a phone number, False otherwise.
    """
    # Regular expression pattern for matching phone numbers
    phone_pattern = re.compile(r'\+?\d{1,3}[- ]?\d{3}[- ]?\d{4}')
    
    # Search for the pattern in the input string
    match = phone_pattern.search(s)
    
    # Return True if a match is found, otherwise False
    return bool(match)
import re
import unittest


class TestPhoneNumberDetection(unittest.TestCase):
    def test_with_international_prefix(self):
        self.assertTrue(is_hava_phone_number("+1-800-555-1234"), "Should detect international prefix")

    def test_with_standard_dashes(self):
        self.assertTrue(is_hava_phone_number("800-555-1234"), "Should detect standard format with dashes")

    def test_with_spaces(self):
        self.assertTrue(is_hava_phone_number("800 555 1234"), "Should detect standard format with spaces")

    def test_without_phone_number(self):
        self.assertFalse(is_hava_phone_number("Hello, world!"), "Should not detect any phone number")

    def test_with_text_containing_numbers(self):
        self.assertTrue(is_hava_phone_number("Call me at 800-555-1234 today!"), "Should detect phone number in text")
if __name__ == '__main__':
    unittest.main()