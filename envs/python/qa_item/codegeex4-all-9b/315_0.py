from urllib.parse import urlparse, parse_qs

def get_file_id_from_url(url: str) -> str:
    """
    Extract the file ID from the given URL query args.

    If not found, return None.

    Args:
        url (str): The URL from which the file ID is to be extracted.

    Returns:
        str: The extracted file ID if present, otherwise None if the URL does not conform to the expected format.

    Example:
        Input: "https://example.com/download?fileId=12345"
        Output: "12345"
    """
    parsed_url = urlparse(url)
    query_args = parse_qs(parsed_url.query)
    file_id = query_args.get('fileId')
    return file_id[0] if file_id else None
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