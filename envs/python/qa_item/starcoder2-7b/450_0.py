import string

def is_valid_password(password: str) -> bool:
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in string.punctuation for char in password):
        return False
    return True
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