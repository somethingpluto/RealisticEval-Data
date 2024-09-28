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