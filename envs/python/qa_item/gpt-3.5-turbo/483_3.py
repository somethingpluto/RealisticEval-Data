import re

def is_valid_email(email: str) -> bool:
    regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(regex, email) is not None
import unittest


class TestEmailValidation(unittest.TestCase):

    def test_valid_email(self):
        self.assertTrue(is_valid_email("test@example.com"))

    def test_valid_email_with_subdomain(self):
        self.assertTrue(is_valid_email("user@subdomain.example.com"))

    def test_valid_email_with_plus_tag(self):
        self.assertTrue(is_valid_email("user.name+tag+sorting@example.com"))

    def test_invalid_email_missing_username(self):
        self.assertFalse(is_valid_email("@missingusername.com"))

    def test_invalid_email_missing_at_symbol(self):
        self.assertFalse(is_valid_email("missingatsign.com"))


    def test_invalid_email_tld_too_short(self):
        self.assertFalse(is_valid_email("user@domain.c"))

    def test_invalid_email_with_special_characters(self):
        self.assertFalse(is_valid_email("user@domain.com!"))


if __name__ == '__main__':
    unittest.main()