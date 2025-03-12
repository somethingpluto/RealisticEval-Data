from datetime import datetime
from typing import Optional

def format_timestamp_to_string(timestamp: float, date_format: Optional[str] = '%a %b %d %I:%M:%S %p %z %Y') -> str:
    """
    Formats the given timestamp as a string according to the specified format, using the system's local time zone.

    Args:
        timestamp (float): The time value representing the seconds since the epoch.
        date_format (Optional[str]): The format string to use for formatting the timestamp.
                                     Defaults to '%a %b %d %I:%M:%S %p %z %Y'.

    Returns:
        str: The formatted date and time string.
    """
    formatted_timestamp = datetime.fromtimestamp(timestamp).strftime(date_format)
    return formatted_timestamp
import unittest
from typing import Optional

class TestFormatTimestampToString(unittest.TestCase):
    def test_basic_functionality(self):
        """Test basic functionality with a known timestamp."""
        timestamp = 1655364000.0  # Corresponds to Thu Jun 16 12:00:00 PM UTC 2022
        # Assuming the local timezone is UTC
        expected_date_str = 'Thu Jun 16 03:20:00 PM +0800 2022'
        self.assertEqual(format_timestamp_to_string(timestamp), expected_date_str, "Should correctly format the timestamp")

    def test_default_format(self):
        """Test using the default format string."""
        timestamp = 1655364000.0
        expected_date_str = 'Thu Jun 16 03:20:00 PM +0800 2022'
        self.assertEqual(format_timestamp_to_string(timestamp), expected_date_str, "Default format should match the expected date string")

    def test_custom_format(self):
        """Test with a custom format string."""
        timestamp = 1655364000.0
        custom_format = '%Y-%m-%d %H:%M:%S'
        expected_date_str = '2022-06-16 15:20:00'
        self.assertEqual(format_timestamp_to_string(timestamp, custom_format), expected_date_str, "Should correctly format the timestamp using the custom format")


    def test_edge_case_boundary_value(self):
        """Test with an edge case timestamp (e.g., Unix epoch start)."""
        timestamp = 0.0  # Unix epoch start
        expected_date_str = 'Thu Jan 01 08:00:00 AM +0800 1970'
        self.assertEqual(format_timestamp_to_string(timestamp), expected_date_str, "Should correctly format the Unix epoch start time")
if __name__ == '__main__':
    unittest.main()