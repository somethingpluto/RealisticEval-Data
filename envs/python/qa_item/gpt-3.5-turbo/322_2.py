import re

def is_valid_email(email: str) -> bool:
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    if re.match(email_pattern, email):
        return True
    else:
        return False
import unittest


class TestIsValidEmail(unittest.TestCase):

    def test_valid_simple_email(self):
        result = is_valid_email('test@example.com')
        self.assertTrue(result)  # 'test@example.com' is a valid email

    def test_valid_email_with_subdomain(self):
        result = is_valid_email('user@mail.example.com')
        self.assertTrue(result)  # 'user@mail.example.com' is a valid email

    def test_invalid_email_missing_at_symbol(self):
        result = is_valid_email('invalid-email.com')
        self.assertFalse(result)  # 'invalid-email.com' is missing the @ symbol

    def test_invalid_email_missing_domain_part(self):
        result = is_valid_email('user@.com')
        self.assertFalse(result)  # 'user@.com' is missing a valid domain name

    def test_invalid_email_with_spaces(self):
        result = is_valid_email('user name@example.com')
        self.assertFalse(result)  # 'user name@example.com' contains spaces

if __name__ == '__main__':
    unittest.main()