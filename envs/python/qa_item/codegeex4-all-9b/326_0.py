from datetime import datetime

def calculate_time_difference(given_date: str) -> dict:
    """
    Calculates the time difference between a given date and the current date.

    Args:
        given_date (str): The date to compare against the current date.

    Returns:
        dict: A dictionary containing days, hours, and minutes elapsed.
              {
                  'days': days,
                  'hours': remaining_hours,
                  'minutes': remaining_minutes,
              }
    """
    # Parse the given date string into a datetime object
    given_date_obj = datetime.strptime(given_date, "%Y-%m-%d")

    # Get the current date and time
    current_date_obj = datetime.now()

    # Calculate the time difference
    time_difference = current_date_obj - given_date_obj

    # Extract days, hours, and minutes from the time difference
    days = time_difference.days
    total_seconds = time_difference.seconds
    hours, remaining_seconds = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remaining_seconds, 60)

    # Return the time difference as a dictionary
    return {
        'days': days,
        'hours': hours,
        'minutes': minutes,
    }
import unittest
from datetime import timedelta, datetime


class TestCalculateTimeDifference(unittest.TestCase):

    def test_should_return_correct_time_difference_for_a_date_in_the_past(self):
        past_date = datetime.now() - timedelta(days=3, minutes=5)  # 3 days and 5 minutes ago
        result = calculate_time_difference(past_date)
        self.assertEqual(result, {'days': 3, 'hours': 0, 'minutes': 5})

    def test_should_return_correct_time_difference_for_a_date_that_is_exactly_now(self):
        now = datetime.now()
        result = calculate_time_difference(now)
        self.assertEqual(result, {'days': 0, 'hours': 0, 'minutes': 0})

    def test_should_return_correct_time_difference_for_a_date_just_seconds_ago(self):
        just_now = datetime.now() - timedelta(seconds=45)  # 45 seconds ago
        result = calculate_time_difference(just_now)
        self.assertEqual(result, {'days': 0, 'hours': 0, 'minutes': 0})

    def test_should_return_correct_time_difference_for_a_date_with_only_hours_difference(self):
        hours_ago = datetime.now() - timedelta(hours=7)  # 7 hours ago
        result = calculate_time_difference(hours_ago)
        self.assertEqual(result, {'days': 0, 'hours': 7, 'minutes': 0})

    def test_should_return_correct_time_difference_for_a_date_with_hours_and_minutes_difference(self):
        hours_and_minutes_ago = datetime.now() - timedelta(days=1, minutes=3)  # 1 day and 3 minutes ago
        result = calculate_time_difference(hours_and_minutes_ago)
        self.assertEqual(result, {'days': 1, 'hours': 0, 'minutes': 3})

if __name__ == '__main__':
    unittest.main()