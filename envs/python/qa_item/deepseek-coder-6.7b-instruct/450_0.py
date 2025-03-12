import string

def is_valid_password(password: str) -> bool:
    """
    Checks whether the provided password meets the specified format requirements:
    - At least one number
    - At least one lowercase letter
    - At least one uppercase letter
    - At least one punctuation mark
    - Minimum length of 8 characters

    Args:
        password (str): The password string to validate.

    Returns:
        bool: Returns True if the password meets all requirements; otherwise, False.
    """
    if len(password) < 8:
        return False
    
    has_number = any(char.isdigit() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_punctuation = any(char in string.punctuation for char in password)
    
    return has_number and has_lowercase and has_uppercase and has_punctuation
import unittest


class TestPasswordValidator(unittest.TestCase):

    def test_valid_password(self):
        self.assertTrue(is_valid_password("Password1!"))

    def test_password_without_number(self):
        self.assertFalse(is_valid_password("Password!"))

    def test_password_without_uppercase(self):
        self.assertFalse(is_valid_password("password1!"))

    def test_password_without_lowercase(self):
        self.assertFalse(is_valid_password("PASSWORD1!"))

    def test_password_without_punctuation(self):
        self.assertFalse(is_valid_password("Password1"))

    def test_password_shorter_than_8_characters(self):
        self.assertFalse(is_valid_password("Pass1!"))

if __name__ == '__main__':
    unittest.main()