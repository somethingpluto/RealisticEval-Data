from typing import Dict, Optional
import re

def convert_csv_values(row: Dict[str, str]) -> Dict[str, Optional[str]]:
    converted_row = {}
    for key, value in row.items():
        try:
            float(value.replace(",", "."))
            converted_row[key] = value.replace(",", ".")
        except ValueError:
            converted_row[key] = None
    return converted_row
import unittest


class TestConvertCsvValues(unittest.TestCase):

    def test_valid_numeric_strings(self):
        """Test with valid numeric strings including commas."""
        row = {'value1': '1,234', 'value2': '5,678', 'value3': '9,876'}
        expected = {'value1': '1.234', 'value2': '5.678', 'value3': '9.876'}
        result = convert_csv_values(row)
        self.assertEqual(result, expected)

    def test_non_numeric_strings(self):
        """Test with non-numeric strings."""
        row = {'value1': 'not_a_number', 'value2': 'hello', 'value3': 'world'}
        expected = {'value1': None, 'value2': None, 'value3': None}
        result = convert_csv_values(row)
        self.assertEqual(result, expected)

    def test_mixed_values(self):
        """Test with a mix of numeric and non-numeric strings."""
        row = {'value1': '1,234', 'value2': 'not_a_number', 'value3': '3,14159'}
        expected = {'value1': '1.234', 'value2': None, 'value3': '3.14159'}
        result = convert_csv_values(row)
        self.assertEqual(result, expected)

    def test_no_values(self):
        row = {'value1': 'aaaa', 'value2': 'not_a_number', 'value3': '3,14'}
        expected = {'value1': None, 'value2': None, 'value3': '3.14'}
        result = convert_csv_values(row)
        self.assertEqual(result, expected)

    def test_edge_cases(self):
        """Test edge cases with empty strings and negative numbers."""
        row = {'value1': '', 'value2': '0.0', 'value3': '1,23'}
        expected = {'value1': None, 'value2': '0.0', 'value3': '1.23'}
        result = convert_csv_values(row)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()