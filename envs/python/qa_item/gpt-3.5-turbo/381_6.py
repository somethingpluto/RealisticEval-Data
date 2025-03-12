import re

def extract_email_details(email: str):
    match = re.match(r'(.*)@(.*)', email)
    if match:
        return match.groups()
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