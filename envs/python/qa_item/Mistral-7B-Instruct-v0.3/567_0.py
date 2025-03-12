from datetime import datetime, timedelta

def get_relative_time(message_date: datetime) -> str:
    now = datetime.now()
    diff = now - message_date

    if diff.days == 0:
        return "Today"
    elif diff.days == 1:
        return "Yesterday"
    elif diff.days < 7:
        day_of_week = message_date.strftime("%A")
        return day_of_week
    else:
        return message_date.strftime("%Y/%m/%d")
import unittest
from datetime import datetime, timedelta
from unittest.mock import patch


class TestGetRelativeTime(unittest.TestCase):

    @patch('datetime.datetime')
    def setUp(self, mock_datetime):
        # Mock the current date to ensure consistent test results
        self.mock_now = datetime(2024, 10, 1)
        mock_datetime.now.return_value = self.mock_now

    def test_should_return_today_for_a_message_created_today(self):
        message_date = datetime.now()  # Current date
        self.assertEqual(get_relative_time(message_date), "Today")

    def test_should_return_yesterday_for_a_message_created_yesterday(self):
        message_date = datetime.now() - timedelta(days=1)  # Yesterday
        self.assertEqual(get_relative_time(message_date), "Yesterday")

    def test_should_return_formatted_date_string_for_a_message_created_10_days_ago(self):
        message_date = datetime.now() - timedelta(days=10)  # 10 days ago
        self.assertEqual(get_relative_time(message_date), "2024/09/21")  # Adjust based on the mock date

    def test_should_return_formatted_date_string_for_a_message_created_15_days_ago(self):
        message_date = datetime.now() - timedelta(days=15)  # 15 days ago
        self.assertEqual(get_relative_time(message_date), "2024/09/16")  # Adjust based on the mock date

if __name__ == '__main__':
    unittest.main()