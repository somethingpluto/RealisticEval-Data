import datetime
import unittest
from unittest.mock import patch


class TestGetCurrentTimeDetails(unittest.TestCase):
    @patch('datetime.datetime')
    def test_start_of_month(self, mock_datetime):
        mock_datetime.now.return_value = datetime.datetime(2023, 9, 1)
        expected = (2023, 9, 1, 4)  # September 1, 2023 is a Friday
        result = get_current_time_details()
        self.assertEqual(result, expected)

    @patch('datetime.datetime')
    def test_middle_of_month(self, mock_datetime):
        mock_datetime.now.return_value = datetime.datetime(2023, 9, 15)
        expected = (2023, 9, 3, 4)  # September 15, 2023 is a Friday
        result = get_current_time_details()
        self.assertEqual(result, expected)

    @patch('datetime.datetime')
    def test_end_of_month(self, mock_datetime):
        mock_datetime.now.return_value = datetime.datetime(2023, 9, 30)
        expected = (2023, 9, 5, 5)  # September 30, 2023 is a Saturday
        result = get_current_time_details()
        self.assertEqual(result, expected)

    @patch('datetime.datetime')
    def test_leap_year_february(self, mock_datetime):
        mock_datetime.now.return_value = datetime.datetime(2024, 2, 29)
        expected = (2024, 2, 5, 3)  # February 29, 2024 is a Thursday
        result = get_current_time_details()
        self.assertEqual(result, expected)

    @patch('datetime.datetime')
    def test_regular_year_february(self, mock_datetime):
        mock_datetime.now.return_value = datetime.datetime(2023, 2, 28)
        expected = (2023, 2, 4, 1)  # February 28, 2023 is a Tuesday
        result = get_current_time_details()
        self.assertEqual(result, expected)
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
