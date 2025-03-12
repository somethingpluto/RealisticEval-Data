from datetime import datetime

def format_date_string(date_str:str):
    try:
        dt_obj = datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S %z (%Z)')
        formatted_date = dt_obj.strftime('%Y-%m-%d_%H:%M:%S')
        return formatted_date
    except ValueError:
        return None
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