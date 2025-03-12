from typing import Dict, Optional

def convert_csv_values(row: Dict[str, str]) -> Dict[str, Optional[str]]:
    """
    Convert numeric values in a CSV row from string format to a standardized format.

    Args:
        row (Dict[str, str]): A dictionary representing a row of CSV data where
                               keys are column names and values are strings.

    Returns:
        Dict[str, Optional[str]]: A new dictionary with values converted:
                                   - Numeric strings have commas replaced with dots.
                                   - Non-numeric strings are set to None.
    """
    converted_row = {}
    
    for key, value in row.items():
        try:
            converted_value = str(value).replace(',', '.')
            converted_value = float(converted_value) if '.' in converted_value else int(converted_value)
        except ValueError:
            converted_value = None
        
        converted_row[key] = converted_value
    
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