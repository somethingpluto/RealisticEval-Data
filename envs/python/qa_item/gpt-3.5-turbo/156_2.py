from typing import List

def format_number(num: float) -> str:
    """
    Format the number into a more readable string representation, returning the original form if the number is less than 1,000.
    If it is greater than or equal to a thousand and less than a million, it is formatted as "x.xK".
    For a million or more, format it as "x.xM".

    Args:
        num (float): The number to be formatted.

    Returns:
        str: The formatted number as a string.
    """ 
    if num < 1000:
        return str(num)
    elif num < 1000000:
        return f"{num/1000:.1f}K"
    else:
        return f"{num/1000000:.1f}M"
import unittest


class TestFormatNumber(unittest.TestCase):
    def test_format_greater_than_equal_to_million(self):
        """should format numbers greater than or equal to 1,000,000 with 'M' suffix"""
        self.assertEqual(format_number(1500000), '1.5M')
        self.assertEqual(format_number(1000000), '1.0M')

    def test_format_greater_than_equal_to_thousand(self):
        """should format numbers greater than or equal to 1,000 but less than 1,000,000 with 'K' suffix"""
        self.assertEqual(format_number(2500), '2.5K')
        self.assertEqual(format_number(1000), '1.0K')

    def test_return_string_if_less_than_thousand(self):
        """should return the number as a string if it is less than 1,000"""
        self.assertEqual(format_number(999), '999')
        self.assertEqual(format_number(500), '500')

    def test_handle_edge_cases(self):
        """should handle edge cases like exactly 1,000 or 1,000,000"""
        self.assertEqual(format_number(1000), '1.0K')
        self.assertEqual(format_number(1000000), '1.0M')

if __name__ == '__main__':
    unittest.main()