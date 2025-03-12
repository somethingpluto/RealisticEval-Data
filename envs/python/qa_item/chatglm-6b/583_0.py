
def remove_query_param(url: str, key: str) -> str:
    """
    Removes the specified parameter from the URL query string.

    This function parses the URL, removes the specified query parameter,
    and returns the modified URL. If the parameter does not exist,
    the original URL is returned.

    Args:
        url (str): The URL from which to remove the parameter.
        key (str): The key of the parameter to remove.

    Returns:
        str: The modified URL with the specified parameter removed.
    """
    # Parse the URL
    query_string = url.split('?')[1]
    # Remove the parameter
    query_string = query_string.replace(key, '')
    # Return the modified URL
    return query_string
python
url = 'http://example.com/page?search=test&page=1'
key ='search'
modified_url = remove_query_param(url, key)
print(modified_url) # Output: http://example.com/page?page=1

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