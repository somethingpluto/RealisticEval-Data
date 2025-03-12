
def get_days_in_month(year: int, month: int) -> int:
    """
    Returns the number of days in a given month of a specific year.

    This function accounts for leap years when calculating the number of days in February.

    Args:
        year (int): The year for which to get the number of days in the month. This should be
                     a valid integer representing a year (e.g., 2024).
        month (int): The month for which to get the number of days. It should be an integer
                      between 1 and 12, where 1 corresponds to January and 12 to December.

    Returns:
        int: The number of days in the specified month of the specified year.
    """
    if month < 2:
        return 0
    if year % 4 == 0 and year % 100!= 0:
        # If the year is a leap year, add 28 to the number of days in February
        return (year + 1) * 28 + (month - 1) * 2
    else:
        # If the year is not a leap year, add 29 to the number of days in February
        return (year + 1) * 29 + (month - 1)

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