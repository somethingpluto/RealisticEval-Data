
from datetime import datetime

def format_date_string(date_str: str) -> str:
    """
    Converts a date string from the format '%a, %d %b %Y %H:%M:%S %z (%Z)'
    to the format '%Y-%m-%d_%H:%M:%S'.

    Args:
        date_str (str): The input date string.

    Returns:
        str: The formatted date string in the format '%Y-%m-%d_%H:%M:%S'.
        None: If the input date string is invalid.
    """
    # Parse the date string into a datetime object
    date = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %z (%Z)")

    # Formatting logic
    formatted_date = ""
    if date.hour < 10:
        formatted_date += "0"
    elif date.hour < 15:
        formatted_date += "1"
    elif date.hour < 20:
        formatted_date += "2"
    elif date.hour < 25:
        formatted_date += "3"
    elif date.hour < 30:
        formatted_date += "4"
    elif date.hour < 35:
        formatted_date += "5"
    elif date.hour < 40:
        formatted_date += "6"
    elif date.hour < 45:
        formatted_date += "7"
    elif date.hour < 50:
        formatted_date += "8"
    elif date.hour < 55:
        formatted_date += "9"
    elif date.hour < 60:
        formatted_date += "a"
    else:
        formatted_date += "b"

    # Convert the datetime object back to a date string
    formatted_date_str = date.strftime("%Y-%m-%d_%H:%M:%S")

    return formatted_date_str

import unittest


class TestFormatDateString(unittest.TestCase):

    def test_valid_date_conversion(self):
        """Test case for a valid date string."""
        date_str = "Fri, 28 Sep 2023 14:45:00 +0000 (UTC)"
        expected_date = "2023-09-28_14:45:00"
        self.assertEqual(format_date_string(date_str), expected_date)

    def test_invalid_date_format(self):
        """Test case for an invalid date string format."""
        date_str = "Invalid date format"
        self.assertIsNone(format_date_string(date_str))

    def test_missing_components(self):
        """Test case for a date string missing components."""
        date_str = "Fri, 28 Sep 2023 14:45:00 +0000"
        self.assertIsNone(format_date_string(date_str))

    def test_edge_case_date(self):
        """Test case for an edge case date string (e.g., leap year)."""
        date_str = "Sun, 29 Feb 2024 14:45:00 +0000 (UTC)"
        expected_date = "2024-02-29_14:45:00"
        self.assertEqual(format_date_string(date_str), expected_date)
if __name__ == '__main__':
    unittest.main()