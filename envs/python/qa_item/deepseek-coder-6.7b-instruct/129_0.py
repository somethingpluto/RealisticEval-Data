import re

def is_valid_url(url: str) -> bool:
    """
    Validates a URL string using a simplified and comprehensive regular expression.

    Args:
        url (str): The URL string to validate.

    Returns:
        bool: True if the URL is valid, False otherwise.
    """
    # Regular expression pattern for a valid URL
    url_pattern = re.compile(
        r'^(https?|ftp)://'  # Scheme (http, https, ftp)
        r'([a-zA-Z0-9.-]+)'  # Host (domain or IP)
        r'(:\d+)?'           # Optional port number
        r'(/[a-zA-Z0-9._~:/?#[\]@!$&\'()*+,;=-]*)?'  # Optional path
        r'(\?[a-zA-Z0-9._~:/?#[\]@!$&\'()*+,;=-]*)?$'  # Optional query string
    )
    
    # Match the URL against the pattern
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