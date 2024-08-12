import re
import unittest


class TestPhoneNumberDetection(unittest.TestCase):
    def test_with_international_prefix(self):
        self.assertTrue(contains_phone_number("+1-800-555-1234"), "Should detect international prefix")

    def test_with_standard_dashes(self):
        self.assertTrue(contains_phone_number("800-555-1234"), "Should detect standard format with dashes")

    def test_with_spaces(self):
        self.assertTrue(contains_phone_number("800 555 1234"), "Should detect standard format with spaces")

    def test_without_phone_number(self):
        self.assertFalse(contains_phone_number("Hello, world!"), "Should not detect any phone number")

    def test_with_text_containing_numbers(self):
        self.assertTrue(contains_phone_number("Call me at 800-555-1234 today!"), "Should detect phone number in text")


def contains_phone_number(output_to_test):
    pattern = r"\+?\d{1,3}[-\s]?\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{2,4}|\(\d{3}\)\s?\d{3}[-\s]?\d{4}"
    return re.search(output_to_test, pattern)

import re


def contains_phone_number(s: str) -> bool:
    """
    Determines whether the string contains a phone number; a possible format for a phone number is +1-800-555-1234, 555-555-1234, 555 555 1234
    """
    # Regex pattern to identify phone numbers
    pattern = r"(\+\d{1,3}[- ]?)?(\d{3}[- ]\d{3}[- ]\d{4})"
    # Use re.search to find a match
    if re.search(pattern, s):
        return True
    else:
        return False
