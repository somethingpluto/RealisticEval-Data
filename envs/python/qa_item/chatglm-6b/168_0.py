
import datetime

def format_date(date_string: str) -> str:
    """
    Converts a date string into a relative time description.
    For example, now time 2024-08-25T12:00:00
         input: 2024-08-24T12:00:00 output: 1 day ago
         input: 2024-08-25T07:00:00 output: 5 hours ago

    Args:
        date_string (str): The date string to convert.

    Returns:
        str: A user-friendly string representing the relative time difference from the current date.
    """
    # Convert date string to datetime object
    datetime_object = datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S")

    # Get current date
    current_date = datetime_object.date()

    # Calculate time difference
    relative_time = current_date - datetime_object

    # Format time difference as string
    return f"{relative_time.strftime('%Y-%m-%d %H:%M:%S')} ago"

import unittest
from datetime import datetime
from unittest.mock import patch


class TestFormatDate(unittest.TestCase):

    def setUp(self, mock_datetime):
        # Set the system time to a fixed date for consistent testing
        mock_datetime.now.return_value = datetime(2024, 8, 25, 12, 0, 0)

    def test_one_day_ago(self):
        date_string = '2024-08-24T12:00:00' 
        result = format_date(date_string)
        self.assertIn(result, ['1 day ago', '24 hours ago'])

    def test_five_hours_ago(self):
        date_string = '2024-08-25T07:00:00'
        result = format_date(date_string)
        self.assertEqual(result, '5 hours ago')

    def test_two_minutes_ago(self):
        date_string = '2024-08-25T11:58:00'
        result = format_date(date_string)
        self.assertEqual(result, '2 minutes ago')

    def test_just_now(self):
        date_string = '2024-08-25T11:59:59'
        result = format_date(date_string)
        self.assertIn(result, ['1 second ago', '1 seconds ago'])

if __name__ == '__main__':
    unittest.main()