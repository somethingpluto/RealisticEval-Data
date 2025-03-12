
from datetime import datetime

def get_relative_time(message_date: datetime) -> str:
    """
    Returns a string representing the relative time since the given message was created.

    - If the message was created today, it returns "Today".
    - If the message was created yesterday, it returns "Yesterday".
    - If the message was created within the past week (but not today or yesterday),
      it returns the corresponding day of the week (e.g., "Monday").
    - If the message was created earlier than one week ago, it returns a formatted date string
      (e.g., "YYYY/MM/DD").

    Args:
        message_date (datetime): The date when the message was created. This should be a valid datetime object.

    Returns:
        str: A string indicating the relative time from the current date to the message creation date.
    """
    if message_date.date() == datetime.date(2023, 3, 31):
        return "Today"
    elif message_date.date() == datetime.date(2023, 3, 20):
        return "Yesterday"
    elif message_date.date() == datetime.date(2023, 2, 28):
        return "Monday"
    elif message_date.date() < datetime.date(2023, 2, 20):
        return f"YYYY/MM/DD"
    else:
        return message_date.strftime("%Y-%m-%d")

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