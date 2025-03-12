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
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return False
    
    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False
    
    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False
    
    # Check for at least one number
    if not re.search(r'\d', password):
        return False
    
    # If all criteria are met, return True
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