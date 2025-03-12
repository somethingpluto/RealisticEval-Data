from datetime import datetime
from typing import Tuple


def get_time_since_born_until_now(birth_date: datetime) -> Tuple[int, int, int, int, int]:
    """
    Calculate the years, months, days, hours, and minutes that have passed
    from the birth date to the current date and return them as a tuple.

    Args:
        birth_date (datetime): The birth date as a datetime object.

    Returns:
        Tuple[int, int, int, int, int]: A tuple containing the values of years, months, days, hours, and minutes.
    """
import unittest
from datetime import datetime, timedelta

# Assuming the function get_time_since_born_until_now is defined here

class TestGetTimeSinceBornUntilNow(unittest.TestCase):

    def setUp(self):
        # Set the system time to a fixed date
        self.fixed_time = datetime(2024, 8, 23, 15, 45)
        # Mock datetime.now() for the tests
        self.original_datetime_now = datetime.now

        def mock_datetime_now():
            return self.fixed_time
        
        datetime.now = mock_datetime_now

    def tearDown(self):
        # Restore original datetime.now
        datetime.now = self.original_datetime_now

    def test_typical_birth_date(self):
        birth_date = datetime(1990, 5, 15, 10, 30)
        result = get_time_since_born_until_now(birth_date)
        self.assertEqual(result, (34, 3, 8, 5, 15))  # 34 years, 3 months, 8 days, 5 hours, 15 minutes

    def test_recent_birth_date(self):
        birth_date = datetime(2024, 8, 20, 12, 0)
        result = get_time_since_born_until_now(birth_date)
        self.assertEqual(result, (0, 0, 3, 3, 45))  # 3 days, 3 hours, 45 minutes

    def test_edge_case_end_of_year(self):
        birth_date = datetime(2023, 12, 31, 23, 59)
        result = get_time_since_born_until_now(birth_date)
        self.assertEqual(result, (0, 7, 22, 15, 46))  # 7 months, 22 days, 15 hours, 46 minutes

    def test_birthday_earlier_in_month(self):
        birth_date = datetime(2024, 8, 1, 0, 0)
        result = get_time_since_born_until_now(birth_date)
        self.assertEqual(result, (0, 0, 22, 15, 45))  # 22 days, 15 hours, 45 minutes

    def test_birthday_later_in_year_before_month(self):
        birth_date = datetime(2024, 1, 1, 1, 0)
        result = get_time_since_born_until_now(birth_date)
        self.assertEqual(result, (0, 7, 22, 14, 45))  # 7 months, 22 days, 14 hours, 45 minutes

    def test_birthday_previous_month(self):
        birth_date = datetime(2024, 7, 30, 10, 0)
        result = get_time_since_born_until_now(birth_date)
        self.assertEqual(result, (0, 0, 24, 5, 45))  # 24 days, 5 hours, 45 minutes
if __name__ == '__main__':
    unittest.main()