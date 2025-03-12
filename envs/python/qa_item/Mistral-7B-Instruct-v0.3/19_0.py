import re

def is_phone_number(s: str) -> bool:
    """
    Determines whether the string contains a phone number.
    A possible format for a phone number is +1-800-555-1234, 555-555-1234, 555 555 1234

    Args:
        s (str): input str maybe contain phone number

    Returns: weather this str contain phone number
    """
    # Regular expression patterns for phone number formats
    patterns = [
        r'\+\d{1,3}-\d{3}-\d{3}-\d{4}',
        r'\(\d{3}\)\s*\d{3}-\d{4}',
        r'\d{3}-\d{3}-\d{4}',
        r'\(\d{3}\)\s*\d{3}\s*\d{4}',
        r'\d{3}\s*\d{3}\s*\d{4}',
        r'\d{4}-\d{3}-\d{4}',
        r'\d{4}\s*\d{3}\s*\d{4}',
    ]

    # Check each pattern
    for pattern in patterns:
        match = re.search(pattern, s)
        if match:
            return True

    # If no match found, return False
    return False
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