import re

def is_valid_url(url: str) -> bool:
    pattern = re.compile(
        r'^(https?|ftp)://[^\s/$.?#].[^\s]*$'
    )
    return bool(pattern.match(url))
import unittest


class TestValidURL(unittest.TestCase):

    def test_validates_standard_http_url(self):
        url = 'http://www.example.com'
        self.assertTrue(is_valid_url(url))

    def test_validates_secure_https_url(self):
        url = 'https://www.example.com'
        self.assertTrue(is_valid_url(url))

    def test_rejects_malformed_url(self):
        url = 'htp:/www.example.com'
        self.assertFalse(is_valid_url(url))

if __name__ == '__main__':
    unittest.main()