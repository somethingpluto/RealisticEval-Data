
import re

def contains_email(text: str) -> bool:
    """
    Check if the given text contains an email address.

    Args:
        text (str): The string to search for an email address.

    Returns:
        bool: True if an email address is found, False otherwise.
    """
    # Use regular expression to search for email addresses
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Check if the text matches the pattern
    return re.search(pattern, text)

import unittest


class TestContainsEmail(unittest.TestCase):

    def test_contains_valid_email(self):
        """Test if a valid email is detected in the string."""
        test_string = "You can reach me at example@example.com for more info."
        self.assertTrue(contains_email(test_string))

    def test_contains_email_with_special_characters(self):
        """Test if an email with special characters is detected."""
        test_string = "My email address is john.doe123+test@gmail.com!"
        self.assertTrue(contains_email(test_string))

    def test_does_not_contain_email(self):
        """Test a string that does not contain any email address."""
        test_string = "This string does not have an email."
        self.assertFalse(contains_email(test_string))

    def test_contains_multiple_emails(self):
        """Test a string containing multiple email addresses."""
        test_string = "You can contact me at example1@example.com or example2@example.com."
        self.assertTrue(contains_email(test_string))

    def test_contains_invalid_email_format(self):
        """Test a string with an invalid email format."""
        test_string = "Please contact me at example@.com or test@domain."
        self.assertFalse(contains_email(test_string))
if __name__ == '__main__':
    unittest.main()