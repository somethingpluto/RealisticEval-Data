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