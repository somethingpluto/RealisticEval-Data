import urllib.parse

def get_file_id_from_url(url: str) -> str:
    query = urllib.parse.urlparse(url).query
    query_dict = urllib.parse.parse_qs(query)
    file_id = query_dict.get('fileId', [None])[0]
    return file_id
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