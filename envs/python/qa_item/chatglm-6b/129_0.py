
def is_valid_url(url: str) -> bool:
    """
    Validates a URL string using a simplified and comprehensive regular expression.

    Args:
        url (str): The URL string to validate.

    Returns:
        bool: True if the URL is valid, False otherwise.
    """
    # Define the regular expression used to validate the URL
    regex = r'https?://\S+'

    # Validate the URL using the regular expression
    if re.match(regex, url):
        return True
    else:
        return False

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