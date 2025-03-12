import re

def extract_email_details(email: str):
    """
    Extracts the username and mailbox suffix from an email address.eg extract_email_details("xxx@gmail.com") returns ('xxx', 'gmail.com')
    Args:
        email (str): the email address to extract details from

    Returns:
        tuple: (username, domain)
    """
    pattern = r'^([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$'
    match = re.match(pattern, email)
    
    if match:
        username = match.group(1)
        domain = match.group(2)
        return (username, domain)
    else:
        return None, None
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