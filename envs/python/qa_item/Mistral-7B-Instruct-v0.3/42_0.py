import re

def replace_phone_numbers(text: str):
    """
    Replace all phone numbers in the string with the string [PHONE_NUM]
    """
    # Define phone number patterns
    patterns = [
        r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',  # (123) 456-7890
        r'\(?\d{3}\)?[-.\s]?\d{4}[-.\s]\d{4}',  # (123) 456-7890 x1234
        r'\d{3}[-.\s]\d{3}[-.\s]\d{4}',  # 123-456-7890
        r'\d{3}[-.\s]\d{4}[-.\s]\d{4}',  # 123-456-7890 x1234
        r'\d{4}[-.\s]\d{4}',  # 1234-5678
        r'\d{3}\s\d{3}\s\d{4}',  # 123 456 7890
        r'\d{3}\s\d{4}\s\d{4}',  # 123 456-7890 x1234
        r'\d{4}\s\d{4}',  # 1234 5678
    ]

    # Replace phone numbers with [PHONE_NUM]
    for pattern in patterns:
        text = re.sub(pattern, '[PHONE_NUM]', text)

    return text
import unittest


class TestReplacePhoneNumbers(unittest.TestCase):
    def test_basic_number(self):
        msg = "Call me at 123-456-7890."
        expected = "Call me at [PHONE_NUM]."
        self.assertEqual(replace_phone_numbers(msg), expected)


    def test_number_with_parentheses(self):
        msg = "Our office number is 123 456-7890."
        expected = "Our office number is [PHONE_NUM]."
        self.assertEqual(replace_phone_numbers(msg), expected)

    def test_number_with_dots(self):
        msg = "Fax us at 123.456.7890."
        expected = "Fax us at [PHONE_NUM]."
        self.assertEqual(replace_phone_numbers(msg), expected)

    def test_no_phone_number(self):
        msg = "Hello, please reply to this email."
        expected = "Hello, please reply to this email."
        self.assertEqual(replace_phone_numbers(msg), expected)

if __name__ == '__main__':
    unittest.main()