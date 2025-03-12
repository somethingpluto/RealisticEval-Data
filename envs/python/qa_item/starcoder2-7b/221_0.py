import ast

def extract_parse_dicts(file_path: str) -> List[Dict]:
    with open(file_path, 'r') as file:
        lines = file.readlines()

    dicts = []
    for line in lines:
        try:
            # Try to parse the line as a Python dictionary
            dicts.append(ast.literal_eval(line))
        except (SyntaxError, ValueError):
            # If the line does not contain a Python dictionary syntax, ignore it
            pass

    return dicts
import unittest
from unittest.mock import mock_open, patch


class TestExtractParseDicts(unittest.TestCase):
    def test_extract_single_valid_dictionary(self):
        mock_content = '{"name": "John", "age": 30}'
        with patch('builtins.open', mock_open(read_data=mock_content)):
            result = extract_parse_dicts('dummy_path')
            self.assertEqual(result, [{"name": "John", "age": 30}])

    def test_extract_multiple_dictionaries(self):
        mock_content = '{"name": "John", "age": 30}\n{"city": "New York", "country": "USA"}'
        with patch('builtins.open', mock_open(read_data=mock_content)):
            result = extract_parse_dicts('dummy_path')
            self.assertEqual(result, [{"name": "John", "age": 30}, {"city": "New York", "country": "USA"}])

    def test_invalid_dictionary_format(self):
        mock_content = '{"name": "John", "age": "thirty"}'
        with patch('builtins.open', mock_open(read_data=mock_content)):
            result = extract_parse_dicts('dummy_path')
            self.assertEqual(result, [{'name': 'John', 'age': 'thirty'}])

    def test_empty_file(self):
        with patch('builtins.open', mock_open(read_data='')):
            result = extract_parse_dicts('dummy_path')
            self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()