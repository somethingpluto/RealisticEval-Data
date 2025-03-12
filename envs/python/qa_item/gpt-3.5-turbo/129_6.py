import re

def is_valid_url(url: str) -> bool:
    url_pattern = re.compile(
        r'^(https?|ftp)://'
        r'((([a-z0-9]([a-z0-9-]*[a-z0-9])?\.)+[a-z]{2,})|((\d{1,3}\.){3}\d{1,3})|localhost)'
        r'(:\d{1,5})?'
        r'(/[-a-z0-9._~%!$&\'()*+,;=:@/]*)?'
        r'(\?[;&a-z0-9._~%!$&\'()*+,;=:@/=-]*)?'
        r'(\#[-a-z0-9._~%!$&\'()*+,;=:@/]*)?$',
        re.IGNORECASE
    )
    
    return bool(url_pattern.match(url))
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