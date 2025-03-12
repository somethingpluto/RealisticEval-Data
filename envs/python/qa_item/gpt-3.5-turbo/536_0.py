from datetime import datetime

def get_date() -> str:
    """
    Gets the current date formatted as 'Month Day, Year'.

    Returns:
        str: The formatted date string.
    """
    now = datetime.now()
    formatted_date = now.strftime("%B %d, %Y")
    
    return formatted_date
import unittest
from datetime import datetime
from unittest.mock import patch


class TestGetDate(unittest.TestCase):

    @patch('datetime.datetime')
    def setUp(self, mock_datetime):
        # Mock the datetime to return a specific date
        mock_datetime.now.return_value = datetime(2024, 10, 1)

    def test_returns_date_in_format(self):
        result = get_date()
        self.assertEqual(result, 'October 1, 2024')

    def test_returns_correct_year(self):
        result = get_date()
        self.assertIn('2024', result)

    def test_returns_correct_month(self):
        result = get_date()
        self.assertIn('October', result)

    def test_returns_correct_day(self):
        result = get_date()
        self.assertIn('1', result)

    def test_returns_date_as_string(self):
        result = get_date()
        self.assertIsInstance(result, str)

    def test_does_not_return_none(self):
        result = get_date()
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()