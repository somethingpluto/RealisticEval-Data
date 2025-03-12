from urllib.parse import urlparse, parse_qs

def get_file_id_from_url(url: str) -> str:
    """Extract the file ID from the given URL query args."""
    try:
        query = urlparse(url).query
        file_id = parse_qs(query)['fileId'][0]
        return file_id
    except (KeyError, TypeError, ValueError):
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