import re

def is_valid_url(url: str) -> bool:
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or IP
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return bool(regex.match(url))
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