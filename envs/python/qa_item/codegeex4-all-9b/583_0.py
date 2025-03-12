from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

def remove_query_param(url: str, key: str) -> str:
    """
    Removes the specified parameter from the URL query string.

    This function parses the URL, removes the specified query parameter,
    and returns the modified URL. If the parameter does not exist,
    the original URL is returned.

    For example:
        - Input: 'http://example.com/page?search=test&page=1', 'search'
        - Output: 'http://example.com/page?page=1'

    Args:
        url (str): The URL from which to remove the parameter.
        key (str): The key of the parameter to remove.

    Returns:
        str: The modified URL with the specified parameter removed.
    """
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    if key in query_params:
        del query_params[key]
        new_query_string = urlencode(query_params, doseq=True)
        return urlunparse(parsed_url._replace(query=new_query_string))
    return url
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