import datetime

def get_current_date_info(test_date: datetime.date) -> dict:
    current_date = test_date if test_date else datetime.date.today()
    
    year = current_date.year
    month = current_date.strftime('%B')
    week_of_the_month = (current_date.day - 1) // 7 + 1
    day_of_the_week = current_date.strftime('%A')
    
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