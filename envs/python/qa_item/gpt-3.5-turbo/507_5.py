import re

def is_strong_password(password: str) -> bool:
    lowercase_regex = re.compile(r'[a-z]')
    uppercase_regex = re.compile(r'[A-Z]')
    number_regex = re.compile(r'\d')

    if len(password) < 8:
        return False
    if not lowercase_regex.search(password):
        return False
    if not uppercase_regex.search(password):
        return False
    if not number_regex.search(password):
        return False

    return True
import unittest


class TestStrongPassword(unittest.TestCase):
    def test_valid_password(self):
        """ Test a strong password that meets all criteria. """
        self.assertTrue(is_strong_password("StrongPass1"))

    def test_missing_lowercase(self):
        """ Test a password missing a lowercase letter. """
        self.assertFalse(is_strong_password("STRONGPASS1"))

    def test_missing_uppercase(self):
        """ Test a password missing an uppercase letter. """
        self.assertFalse(is_strong_password("strongpass1"))

    def test_missing_number(self):
        """ Test a password missing a number. """
        self.assertFalse(is_strong_password("StrongPassword"))

    def test_too_short(self):
        """ Test a password that is too short. """
        self.assertFalse(is_strong_password("Short1"))

    def test_valid_with_special_characters(self):
        """ Test a password that includes special characters but is still strong. """
        self.assertTrue(is_strong_password("Strong!Password1"))
if __name__ == '__main__':
    unittest.main()