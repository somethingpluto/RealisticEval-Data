import unittest


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

    def test_end_of_month(self):
        result = get_current_date_info(datetime.date(2023, 1, 31))
        expected = {
            'year': 2023,
            'month': 'January',
            'week_of_the_month': 6,
            'day_of_the_week': 'Tuesday'
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

import datetime
import calendar


def get_current_date_info(test_date=None):
    """
    Returns the current time information including year, month, week of the month, and day of the week.
    Optionally takes a date object for testing purposes.

    Args:
        test_date (datetime.date): The date to compute information for, defaults to today's date if not provided.

    Returns:
        dict: A dictionary containing the year, month, week of the month, and day of the week.
    """
    if test_date is None:
        today = datetime.date.today()
    else:
        today = test_date

    year = today.year
    month = today.month
    day_of_week = calendar.day_name[today.weekday()]

    # Calculate the week of the month
    first_day_of_month = today.replace(day=1)
    first_day_weekday = first_day_of_month.weekday()
    week_of_month = (today.day + first_day_weekday - 1) // 7 + 1

    return {
        'year': year,
        'month': calendar.month_name[month],
        'week_of_the_month': week_of_month,
        'day_of_the_week': day_of_week
    }