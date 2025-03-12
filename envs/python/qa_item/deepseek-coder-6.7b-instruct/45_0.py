import datetime

def get_current_date_info(test_date: datetime.date) -> dict:
    """
    Returns the current time information including year, month, week of the month, and day of the week.

    Args:
        test_date (datetime.date): The date to compute information for.

    Returns:
        dict: A dictionary containing the year, month, week of the month, and day of the week.
    """
    # Get the year
    year = test_date.year
    
    # Get the month name
    month = test_date.strftime('%B')
    
    # Calculate the week of the month
    first_day_of_month = test_date.replace(day=1)
    week_of_the_month = (test_date.day + first_day_of_month.weekday() - 1) // 7 + 1
    
    # Get the day of the week
    day_of_the_week = test_date.strftime('%A')
    
    return {
        'year': year,
        'month': month,
        'week_of_the_month': week_of_the_month,
        'day_of_the_week': day_of_the_week
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