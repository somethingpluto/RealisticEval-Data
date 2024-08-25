import unittest
from unittest.mock import patch
import datetime
import calendar


class TestGetCurrentDateInfo(unittest.TestCase):

    @patch('datetime.date')
    def test_beginning_of_month(self, mock_date):
        # Mocking the date to be the first of the month
        mock_date.today.return_value = datetime.date(2023, 8, 1)
        expected = {
            'year': 2023,
            'month': 'August',
            'week_of_the_month': 1,
            'day_of_the_week': 'Tuesday'
        }
        result = get_current_date_info()
        self.assertEqual(result, expected)

    @patch('datetime.date')
    def test_end_of_month(self, mock_date):
        # Mocking the date to be the end of the month
        mock_date.today.return_value = datetime.date(2023, 8, 31)
        expected = {
            'year': 2023,
            'month': 'August',
            'week_of_the_month': 5,
            'day_of_the_week': 'Thursday'
        }
        result = get_current_date_info()
        self.assertEqual(result, expected)

    @patch('datetime.date')
    def test_middle_of_month(self, mock_date):
        # Mocking the date to be mid-month
        mock_date.today.return_value = datetime.date(2023, 8, 15)
        expected = {
            'year': 2023,
            'month': 'August',
            'week_of_the_month': 3,
            'day_of_the_week': 'Tuesday'
        }
        result = get_current_date_info()
        self.assertEqual(result, expected)

    @patch('datetime.date')
    def test_leap_year_february(self, mock_date):
        # Testing for leap year February scenario
        mock_date.today.return_value = datetime.date(2024, 2, 29)
        expected = {
            'year': 2024,
            'month': 'February',
            'week_of_the_month': 5,
            'day_of_the_week': 'Thursday'
        }
        result = get_current_date_info()
        self.assertEqual(result, expected)

    @patch('datetime.date')
    def test_new_year(self, mock_date):
        # Testing the transition to a new year
        mock_date.today.return_value = datetime.date(2024, 1, 1)
        expected = {
            'year': 2024,
            'month': 'January',
            'week_of_the_month': 1,
            'day_of_the_week': 'Monday'
        }
        result = get_current_date_info()
        self.assertEqual(result, expected)
