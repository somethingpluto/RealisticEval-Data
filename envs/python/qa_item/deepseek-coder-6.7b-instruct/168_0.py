from datetime import datetime, timedelta

def format_date(date_string: str) -> str:
    """
    Converts a date string into a relative time description.

    Args:
        date_string (str): The date string to convert.

    Returns:
        str: A user-friendly string representing the relative time difference from the current date.
    """
    # Parse the input date string
    input_date = datetime.fromisoformat(date_string)
    
    # Get the current date and time
    current_date = datetime.now()
    
    # Calculate the difference between the current date and the input date
    delta = current_date - input_date
    
    # Determine the appropriate time unit and value
    if delta.days > 0:
        if delta.days == 1:
            return "1 day ago"
        else:
            return f"{delta.days} days ago"
    elif delta.seconds >= 3600:
        hours = delta.seconds // 3600
        if hours == 1:
            return "1 hour ago"
        else:
            return f"{hours} hours ago"
    elif delta.seconds >= 60:
        minutes = delta.seconds // 60
        if minutes == 1:
            return "1 minute ago"
        else:
            return f"{minutes} minutes ago"
    else:
        return "just now"
import unittest
from datetime import datetime
from unittest.mock import patch


class TestFormatDate(unittest.TestCase):

    @patch('your_module.datetime')
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