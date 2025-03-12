import re

def get_file_id_from_url(url: str) -> str:
    """Extract the file ID from the given URL query args."""
    # Check if the URL contains a '?' character to ensure it has query parameters
    if '?' not in url:
        return None

    # Split the URL into parts using '?' as the delimiter
    url_parts = url.split('?')

    # Ensure the second part exists (contains query parameters)
    if len(url_parts) < 2:
        return None

    # Split the query parameters into a dictionary
    query_params = dict(x.split('=') for x in url_parts[1].split('&'))

    # Check if 'fileId' exists as a key in the query parameters dictionary
    if 'fileId' in query_params:
        return query_params['fileId']

    # If 'fileId' is not found, return None
    return None
import unittest


class TestGetFileIdFromUrl(unittest.TestCase):
    def test_valid_url_with_fileId(self):
        url = 'https://example.com/download?fileId=12345'
        self.assertEqual(get_file_id_from_url(url), '12345')

    def test_missing_fileId_parameter(self):
        url = 'https://example.com/download'
        self.assertIsNone(get_file_id_from_url(url))

    def test_empty_fileId_parameter(self):
        url = 'https://example.com/download?fileId='
        self.assertIsNone(get_file_id_from_url(url))

    def test_malformed_url(self):
        url = 'https://example.com/download?fileId=12345&otherParam'
        self.assertEqual(get_file_id_from_url(url), '12345')  # Adjust based on the actual implementation

if __name__ == '__main__':
    unittest.main()