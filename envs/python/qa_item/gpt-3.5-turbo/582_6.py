from urllib.parse import urlencode

def to_query_string(params: dict) -> str:
    return '?' + urlencode(params) if params else ''
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