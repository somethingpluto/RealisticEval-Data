from datetime import date, timedelta, day
from calendar import isleap

def get_current_date_info(test_date=None):
    if test_date is None:
        test_date = date.today()

    weekday = test_date.strftime('%A')
    month = test_date.strftime('%B')
    day = test_date.day

    year = test_date.year
    is_leap_year = isleap(year)

    jan_1 = date(year, 1, 1)
    days_in_year = jan_1.isocalendar()[1]
    days_in_month = test_date.isocalendar()[2]

    week_of_the_month = (test_date - jan_1 + timedelta(days=4)).isocalendar()[1]

    return {
        'year': year,
       'month': month,
        'week_of_the_month': week_of_the_month,
        'day_of_the_week': weekday,
        'day_of_the_year': days_in_month + (week_of_the_month - 1) * 7
    }
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