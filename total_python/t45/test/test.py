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