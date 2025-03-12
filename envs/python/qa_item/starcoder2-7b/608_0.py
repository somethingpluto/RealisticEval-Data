import re

def is_valid_email(email: str) -> bool:
    """Checks whether the given string is a valid email address.

    Args:
        email (str): The string to be checked.

    Returns:
        bool: True if the string is a valid email address, False otherwise.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_regex, email))
import unittest

class TestValidEmail(unittest.TestCase):

    def test_valid_email_1(self):
        self.assertTrue(is_valid_email("example@test.com"), "Valid email should return true")

    def test_valid_email_2(self):
        self.assertTrue(is_valid_email("user.name+tag+sorting@example.com"), "Valid email should return true")

    def test_valid_email_3(self):
        self.assertTrue(is_valid_email("user@subdomain.example.com"), "Valid email with subdomain should return true")

    def test_invalid_email_1(self):
        self.assertFalse(is_valid_email("invalid-email@.com"), "Invalid email should return false")

    def test_invalid_email_2(self):
        self.assertFalse(is_valid_email("invalid@domain@domain.com"), "Invalid email should return false")

    def test_null_email(self):
        self.assertFalse(is_valid_email(None), "Null email should return false")

if __name__ == '__main__':
    unittest.main()