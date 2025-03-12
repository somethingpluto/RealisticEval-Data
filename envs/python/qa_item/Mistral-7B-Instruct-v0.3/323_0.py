import re

def is_valid_username(username: str) -> bool:
    """
    Verify that a string is a valid username and check that the username contains only letters, numbers, and underscores.

    Args:
        username (str): The username to be validated.

    Returns:
        bool: True if the username matches the regex pattern, indicating it is valid;False if the username contains any characters outside of letters, numbers, and underscores.
    """
    pattern = r'^[a-zA-Z0-9_]+$'
    return re.match(pattern, username) is not None
import unittest


class TestUsernameValidation(unittest.TestCase):

    def test_valid_username_with_letters_numbers_and_underscores(self):
        result = is_valid_username('user_123')
        self.assertEqual(result, True)  # 'user_123' is a valid username

    def test_valid_username_with_only_letters(self):
        result = is_valid_username('username')
        self.assertEqual(result, True)  # 'username' is a valid username

    def test_invalid_username_with_special_characters(self):
        result = is_valid_username('user-name')
        self.assertEqual(result, False)  # 'user-name' contains a hyphen

    def test_invalid_username_with_spaces(self):
        result = is_valid_username('user name')
        self.assertEqual(result, False)  # 'user name' contains spaces

    def test_valid_username_with_only_numbers(self):
        result = is_valid_username('12345')
        self.assertEqual(result, True)  # '12345' is a valid username

if __name__ == '__main__':
    unittest.main()