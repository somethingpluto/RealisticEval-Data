from dateutil import parser
from datetime import datetime, timedelta

def format_date(date_string: str) -> str:
    date = parser.parse(date_string)
    now = datetime.now()
    delta = now - date

    if delta.days > 0:
        return f"{delta.days} days ago"
    elif delta.seconds > 3600:
        return f"{delta.seconds // 3600} hours ago"
    else:
        return f"{delta.seconds // 60} minutes ago"
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