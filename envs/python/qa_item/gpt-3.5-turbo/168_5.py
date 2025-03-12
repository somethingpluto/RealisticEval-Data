from datetime import datetime

def format_date(date_string: str) -> str:
    current_date = datetime.now()
    input_date = datetime.fromisoformat(date_string)

    time_difference = current_date - input_date

    if time_difference.days > 0:
        return f"{time_difference.days} day{'s' if time_difference.days > 1 else ''} ago"
    else:
        hours = time_difference.seconds // 3600
        if hours > 0:
            return f"{hours} hour{'s' if hours > 1 else ''} ago"
        else:
            minutes = time_difference.seconds // 60
            if minutes > 0:
                return f"{minutes} minute{'s' if minutes > 1 else ''} ago"
            else:
                return "Just now"
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