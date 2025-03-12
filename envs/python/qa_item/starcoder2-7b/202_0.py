def get_days_in_month(year: int, month: int) -> int:
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29
        else:
            return 28
    else:
        raise ValueError("Invalid month. Month should be between 1 and 12.")
import unittest


class Tester(unittest.TestCase):

    def test_leap_year_february(self):
        """Test for leap year February."""
        self.assertEqual(get_days_in_month(2024, 2), 29)  # 2024 is a leap year

    def test_non_leap_year_february(self):
        """Test for non-leap year February."""
        self.assertEqual(get_days_in_month(2023, 2), 28)  # 2023 is not a leap year

    def test_month_with_31_days(self):
        """Test for months with 31 days."""
        self.assertEqual(get_days_in_month(2023, 1), 31)  # January has 31 days
        self.assertEqual(get_days_in_month(2023, 7), 31)  # July has 31 days

    def test_month_with_30_days(self):
        """Test for months with 30 days."""
        self.assertEqual(get_days_in_month(2023, 4), 30)  # April has 30 days
        self.assertEqual(get_days_in_month(2023, 11), 30) # November has 30 days

    def test_invalid_month(self):
        """Test for invalid months."""
        with self.assertRaises(InvalidMonthError):
            get_days_in_month(2023, 0)  # Month less than 1
        with self.assertRaises(InvalidMonthError):
            get_days_in_month(2023, 13)  # Month greater than 12

if __name__ == '__main__':
    unittest.main()