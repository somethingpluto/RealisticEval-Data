
import datetime

def get_current_date_info(test_date: datetime.date) -> dict:
    """
    Returns the current time information including year, month, week of the month, and day of.eg {
            'year': 2024,
           'month': 'February',
            'week_of_the_month': 5,
            'day_of_the_week': 'Thursday'
        }

    Args:
        test_date (datetime.date): The date to compute information for, defaults to today's date if not provided.

    Returns:
        dict: A dictionary containing the year, month, week of the month, and day of the week.
    """
    current_date = datetime.date.today()
    current_date_str = current_date.strftime('%Y-%m-%d')
    info = {
        'year': current_date_str[:4],
       'month': current_date_str[4:6],
        'week_of_the_month': current_date_str[6:8],
        'day_of_the_week': current_date_str[8:]
    }
    return info

import unittest
import datetime


class TestGetCurrentDateInfo(unittest.TestCase):

    def test_beginning_of_month(self):
        result = get_current_date_info(datetime.date(2023, 1, 1))
        expected = {
            'year': 2023,
            'month': 'January',
            'week_of_the_month': 1,
            'day_of_the_week': 'Sunday'
        }
        self.assertEqual(result, expected)

    def test_middle_of_month(self):
        result = get_current_date_info(datetime.date(2023, 1, 15))
        expected = {
            'year': 2023,
            'month': 'January',
            'week_of_the_month': 3,
            'day_of_the_week': 'Sunday'
        }
        self.assertEqual(result, expected)

    def test_leap_year(self):
        result = get_current_date_info(datetime.date(2024, 2, 29))
        expected = {
            'year': 2024,
            'month': 'February',
            'week_of_the_month': 5,
            'day_of_the_week': 'Thursday'
        }
        self.assertEqual(result, expected)

    def test_change_of_year(self):
        result = get_current_date_info(datetime.date(2022, 12, 31))
        expected = {
            'year': 2022,
            'month': 'December',
            'week_of_the_month': 5,
            'day_of_the_week': 'Saturday'
        }
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()