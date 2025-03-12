def to_query_string(params: dict) -> str:
    """
    Converts a dictionary of parameters to a query string.

    For example:
        - Input: {'search': 'test', 'page': 1, 'size': 10}
        - Output: '?search=test&page=1&size=10'

    Args:
        params (dict): The parameters to convert. The keys should be strings
                       and values can be of any type that can be converted to a string.

    Returns:
        str: The query string representation of the parameters.
    """
    query_string = '?'
    for key, value in params.items():
        query_string += f'{key}={str(value)}&'
    return query_string.rstrip('&')
import unittest


class TestToQueryString(unittest.TestCase):

    def test_convert_simple_object_to_query_string(self):
        params = {'search': 'test', 'page': 1, 'size': 10}
        result = to_query_string(params)
        self.assertEqual(result, '?search=test&page=1&size=10')

    def test_encode_special_characters_in_query_string(self):
        params = {'search': 'hello world', 'filter': 'price < \$50'}
        result = to_query_string(params)
        self.assertEqual(result, '?search=hello%20world&filter=price%20%3C%20%2450')

    def test_handle_empty_string_values(self):
        params = {'search': '', 'page': 1}
        result = to_query_string(params)
        self.assertEqual(result, '?search=&page=1')

    def test_handle_boolean_values(self):
        params = {'isActive': True, 'isVerified': False}
        result = to_query_string(params)
        self.assertEqual(result, '?isActive=True&isVerified=False')


if __name__ == '__main__':
    unittest.main()