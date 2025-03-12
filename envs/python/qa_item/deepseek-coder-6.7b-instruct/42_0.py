import re

def replace_phone_numbers(text: str) -> str:
    """
    Replace all phone numbers in the string with the string [PHONE_NUM].

    Args:
        text (str): The input string that may contain phone numbers.

    Returns:
        str: The modified string with phone numbers replaced by '[PHONE_NUM]'.
    """
    # Regular expression to match common phone number formats
    phone_regex = re.compile(r'''
        \b
        (?:
            \+?(\d{1,3})?            # Country code (optional)
            [\s-]?                    # Separator (optional)
            \(?(\d{3})\)?             # Area code (optional)
            [\s-]?                    # Separator (optional)
            (\d{3})                   # First 3 digits
            [\s-]?                    # Separator (optional)
            (\d{4})                   # Last 4 digits
        )
        \b
    ''', re.VERBOSE)
    
    # Replace all matched phone numbers with [PHONE_NUM]
    return phone_regex.sub('[PHONE_NUM]', text)
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