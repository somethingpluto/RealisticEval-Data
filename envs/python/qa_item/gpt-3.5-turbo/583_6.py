from urllib.parse import urlparse, urlencode

def remove_query_param(url: str, key: str) -> str:
    parsed_url = urlparse(url)
    query_params = parsed_url.query
    query_dict = dict(x.split('=') for x in query_params.split('&') if '=' in x)

    if key in query_dict:
        del query_dict[key]

    new_query_params = urlencode(query_dict)
    new_url = parsed_url._replace(query=new_query_params).geturl()

    return new_url
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