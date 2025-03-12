import re

def is_valid_username(username: str) -> bool:
    """
    Checks whether the provided username is valid.
    A valid username is defined as a string that:
    - Has a length between 5 and 16 characters (inclusive).
    - Contains only alphanumeric characters (letters and digits) and spaces.

    Args:
        username (str): The username to validate.

    Returns:
        bool: Returns True if the username is valid; otherwise, False.
    """
    # Check length
    if not (5 <= len(username) <= 16):
        return False
    
    # Check for alphanumeric characters and spaces
    if not re.match(r'^[a-zA-Z0-9 ]+$', username):
        return False
    
    return True
import unittest


class TestIsValidUsername(unittest.TestCase):

    def test_valid_username_with_alphanumeric_characters(self):
        self.assertTrue(is_valid_username('User123'))

    def test_valid_username_with_spaces(self):
        self.assertTrue(is_valid_username('User 123'))

    def test_invalid_username_that_is_too_short(self):
        self.assertFalse(is_valid_username('User'))

    def test_invalid_username_that_is_too_long(self):
        self.assertFalse(is_valid_username('ThisIsAVeryLongUsername'))

    def test_invalid_username_with_special_characters(self):
        self.assertFalse(is_valid_username('User!'))

    def test_invalid_username_with_only_spaces(self):
        self.assertFalse(is_valid_username('     '))

    def test_invalid_input_type_number(self):
        self.assertFalse(is_valid_username(12345))
if __name__ == '__main__':
    unittest.main()