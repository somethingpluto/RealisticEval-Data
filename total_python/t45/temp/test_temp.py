import unittest
from unittest.mock import patch
import datetime
from typing import Tuple

class TestGetCurrentTimeDetails(unittest.TestCase):

    @patch('datetime.datetime')
    def test_first_day_of_month(self, mock_datetime):
        # Mock the date to the first day of a month
        mock_datetime.now.return_value = datetime.datetime(2024, 8, 1)
        mock_datetime.now.side_effect = lambda: mock_datetime.now.return_value

        result = get_current_time_details()
        self.assertEqual(result, (2024, 8, 1, 3))  # August 1st, 2024 is a Thursday (day 3), first week of the month

    @patch('datetime.datetime')
    def test_middle_of_month(self, mock_datetime):
        # Mock the date to the middle of a month
        mock_datetime.now.return_value = datetime.datetime(2024, 8, 15)
        mock_datetime.now.side_effect = lambda: mock_datetime.now.return_value

        result = get_current_time_details()
        self.assertEqual(result, (2024, 8, 3, 3))  # August 15th, 2024 is a Thursday, third week of the month

    @patch('datetime.datetime')
    def test_last_day_of_month(self, mock_datetime):
        # Mock the date to the last day of a month
        mock_datetime.now.return_value = datetime.datetime(2024, 8, 31)
        mock_datetime.now.side_effect = lambda: mock_datetime.now.return_value

        result = get_current_time_details()
        self.assertEqual(result, (2024, 8, 5, 5))  # August 31st, 2024 is a Saturday (day 5), fifth week of the month

    @patch('datetime.datetime')
    def test_first_day_of_week(self, mock_datetime):
        # Mock the date to the first day of the week (Monday)
        mock_datetime.now.return_value = datetime.datetime(2024, 8, 5)
        mock_datetime.now.side_effect = lambda: mock_datetime.now.return_value

        result = get_current_time_details()
        self.assertEqual(result, (2024, 8, 2, 0))  # August 5th, 2024 is a Monday (day 0), second week of the month

    @patch('datetime.datetime')
    def test_leap_year_february(self, mock_datetime):
        # Mock the date to February 29th of a leap year
        mock_datetime.now.return_value = datetime.datetime(2024, 2, 29)
        mock_datetime.now.side_effect = lambda: mock_datetime.now.return_value

        result = get_current_time_details()
        self.assertEqual(result, (2024, 2, 5, 3))  # February 29th, 2024 is a Thursday (day 3), fifth week of the month
import datetime
import calendar
from typing import Tuple


def get_current_time_details() -> Tuple[int, int, int, int]:
    """
    Get the current year, month, week of the month, and day of the week.

    :return: A dictionary containing the current year, month, week of the month, and day of the week.
    """
    now = datetime.datetime.now()

    # Get the current year and month
    year = now.year
    month = now.month

    # Calculate the day of the week (0=Monday, 6=Sunday)
    day_of_week = now.weekday()

    # Calculate the first day of the month and today's day
    first_day_of_month = now.replace(day=1)
    day_of_month = now.day

    # Calculate the week of the month
    _, days_in_month = calendar.monthrange(year, month)
    weeks_in_month = [calendar.monthcalendar(year, month)[i] for i in range(5)]
    week_of_month = 0
    for week in weeks_in_month:
        if day_of_month in week:
            week_of_month = weeks_in_month.index(week) + 1
            break

    return year, month, week_of_month, day_of_week
