def is_hava_phone_number(s: str) -> bool:
    """
    determines whether the string contains a phone number; a possible format for a phone number is +1-800-555-1234, 555-555-1234, 555 555 1234
    Args:
        s (str): input str maybe contain phone number

    Returns: weather this str contain phone number

    """
    import re
    phone_number_pattern = re.compile(r'''
        (\+1-)?               # optional country code
        (\()?                # optional opening parenthesis
        \d{3}                # area code
        (\))?                # optional closing parenthesis
        [-\s]?               # separator
        \d{3}                # central office code
        [-\s]?               # separator
        \d{4}                # line number
    ''', re.VERBOSE)
    return bool(phone_number_pattern.search(s))
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