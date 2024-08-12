import datetime
import unittest
from unittest.mock import patch


class TestGetCurrentTimeDetails(unittest.TestCase):

    @patch('datetime.datetime')
    def test_specific_date(self, mock_datetime):
        # Mock datetime to return February 15, 2022
        mock_datetime.now.return_value = datetime.datetime(2022, 2, 15)
        expected_year = 2022
        expected_month = 2
        expected_week_of_month = 3  # February 1, 2022, is a Tuesday
        expected_weekday = 'Tuesday'

        result = get_current_time_details()

        self.assertEqual(result, (expected_year, expected_month, expected_week_of_month, expected_weekday))

    @patch('datetime.datetime')
    def test_end_of_month(self, mock_datetime):
        # Test for the last day of the month
        mock_datetime.now.return_value = datetime.datetime(2022, 7, 31)
        expected_year = 2022
        expected_month = 7
        expected_week_of_month = 5
        expected_weekday = 'Sunday'

        result = get_current_time_details()

        self.assertEqual(result, (expected_year, expected_month, expected_week_of_month, expected_weekday))

    @patch('datetime.datetime')
    def test_start_of_month(self, mock_datetime):
        # Test for the first day of the month
        mock_datetime.now.return_value = datetime.datetime(2021, 9, 1)
        expected_year = 2021
        expected_month = 9
        expected_week_of_month = 1
        expected_weekday = 'Wednesday'

        result = get_current_time_details()

        self.assertEqual(result, (expected_year, expected_month, expected_week_of_month, expected_weekday))

    @patch('datetime.datetime')
    def test_middle_of_month(self, mock_datetime):
        # Test for the middle of the month
        mock_datetime.now.return_value = datetime.datetime(2020, 12, 15)
        expected_year = 2020
        expected_month = 12
        expected_week_of_month = 3
        expected_weekday = 'Tuesday'

        result = get_current_time_details()

        self.assertEqual(result, (expected_year, expected_month, expected_week_of_month, expected_weekday))

    @patch('datetime.datetime')
    def test_leap_year(self, mock_datetime):
        # Test for a date in a leap year
        mock_datetime.now.return_value = datetime.datetime(2020, 2, 29)
        expected_year = 2020
        expected_month = 2
        expected_week_of_month = 5
        expected_weekday = 'Saturday'

        result = get_current_time_details()

        self.assertEqual(result, (expected_year, expected_month, expected_week_of_month, expected_weekday))