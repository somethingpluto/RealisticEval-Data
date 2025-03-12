
import re

def is_strong_password(password: str) -> bool:
    """
    Check if the provided password is strong.

    A strong password must satisfy the following criteria:
    - At least one lowercase letter
    - At least one uppercase letter
    - At least one number
    - At least 8 characters long

    Args:
        password (str): The password to check.

    Returns:
        bool: True if the password is strong, False otherwise.
    """
    # Validate the length of the password
    if len(password) < 8:
        return False

    # Check if the password contains any uppercase letters
    uppercase_letters = re.findall(r' uppercase\b', password)
    if uppercase_letters == []:
        return False

    # Check if the password contains any lowercase letters
    lowercase_letters = re.findall(r' lowercase\b', password)
    if lowercase_letters == []:
        return False

    # Check if the password contains any numbers
    numeric_letters = re.findall(r'\d+', password)
    if numeric_letters == []:
        return False

    # Check if the password contains any special characters
    special_letters = re.findall(r'\S+', password)
    if special_letters == []:
        return False

    # Check if the password is at least 8 characters long
    return len(password) >= 8

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