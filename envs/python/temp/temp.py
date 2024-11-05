def extract_email_details(email):
    """
    Extracts the username and mailbox suffix from an email address.

    :param email: str, the email address to extract details from
    :return: tuple, (username, domain) where:
        username is the part before '@'
        domain is the part after '@'

    Example:
        extract_email_details("xxx@gmail.com") returns ('xxx', 'gmail.com')
    """
    # Check if '@' is in the email
    if '@' not in email:
        raise ValueError("Invalid email address. Email must contain an '@' character.")

    # Split the email at the '@' and assign parts to username and domain
    username, domain = email.split('@', 1)

    return username, domain
import unittest

class TestExtractEmailDetails(unittest.TestCase):

    def test_valid_email(self):
        # Test with a typical email address
        email = "user@example.com"
        expected = ("user", "example.com")
        result = extract_email_details(email)
        self.assertEqual(result, expected)

    def test_valid_email_with_subdomain(self):
        # Test with an email that includes a subdomain
        email = "user@mail.office.com"
        expected = ("user", "mail.office.com")
        result = extract_email_details(email)
        self.assertEqual(result, expected)


    def test_email_without_at_symbol(self):
        # Test with an email that lacks an '@' symbol
        email = "userexample.com"
        with self.assertRaises(ValueError):
            extract_email_details(email)

    def test_empty_email(self):
        # Test with an empty string as an email
        email = ""
        with self.assertRaises(ValueError):
            extract_email_details(email)
if __name__ == '__main__':
    unittest.main()