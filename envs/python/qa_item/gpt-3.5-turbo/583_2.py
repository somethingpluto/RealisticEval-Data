from urllib.parse import urlparse, urlencode, parse_qsl, urlunparse

def remove_query_param(url: str, key: str) -> str:
    parsed_url = urlparse(url)
    query_params = parse_qsl(parsed_url.query)
    filtered_params = [(k, v) for k, v in query_params if k != key]
    modified_query = urlencode(filtered_params)
    
    modified_url = parsed_url._replace(query=modified_query)
    
    return urlunparse(modified_url)
import unittest


class TestRemoveQueryParam(unittest.TestCase):

    def test_remove_existing_parameter(self):
        url = 'https://example.com?page=1&sort=asc&filter=red'
        result = remove_query_param(url, 'sort')
        self.assertEqual(result, 'https://example.com/?page=1&filter=red')

    def test_no_modification_if_parameter_does_not_exist(self):
        url = 'https://example.com?page=1&filter=red'
        result = remove_query_param(url, 'sort')
        self.assertEqual(result, 'https://example.com/?page=1&filter=red')

    def test_return_original_url_if_no_query_parameters(self):
        url = 'https://example.com'
        result = remove_query_param(url, 'sort')
        self.assertEqual(result, 'https://example.com/')

    def test_remove_multiple_occurrences_of_a_parameter(self):
        url = 'https://example.com?page=1&filter=red&filter=blue'
        result = remove_query_param(url, 'filter')
        self.assertEqual(result, 'https://example.com/?page=1')

    def test_handle_encoded_characters_in_parameter(self):
        url = 'https://example.com?page=1&sort=asc&filter=hello%20world'
        result = remove_query_param(url, 'filter')
        self.assertEqual(result, 'https://example.com/?page=1&sort=asc')

    def test_handle_case_when_parameter_is_only_one_in_url(self):
        url = 'https://example.com?sort=asc'
        result = remove_query_param(url, 'sort')
        self.assertEqual(result, 'https://example.com/')

if __name__ == '__main__':
    unittest.main()