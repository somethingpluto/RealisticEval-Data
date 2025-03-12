from datetime import datetime

def format_date(date_string: str) -> str:
    current_date = datetime.now()
    date_time = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S")
    
    time_difference = current_date - date_time
    
    days = time_difference.days
    seconds = time_difference.seconds
    
    if days > 0:
        if days == 1:
            return f"{days} day ago"
        else:
            return f"{days} days ago"
    else:
        hours = seconds // 3600
        if hours > 0:
            if hours == 1:
                return f"{hours} hour ago"
            else:
                return f"{hours} hours ago"
        else:
            minutes = seconds // 60
            if minutes == 1:
                return f"{minutes} minute ago"
            else:
                return f"{minutes} minutes ago"
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