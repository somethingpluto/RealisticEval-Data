import re

def is_valid_password(password: str) -> bool:
    if len(password) < 8:
        return False

    has_number = re.search(r"\d", password)
    has_lowercase = re.search(r"[a-z]", password)
    has_uppercase = re.search(r"[A-Z]", password)
    has_punctuation = re.search(r"[^a-zA-Z0-9\s]", password)

    if has_number and has_lowercase and has_uppercase and has_punctuation:
        return True
    else:
        return False
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