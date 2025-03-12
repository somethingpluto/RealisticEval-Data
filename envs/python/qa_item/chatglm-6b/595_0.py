
def get_days_in_month(year: int, month: int) -> int:
    """
    Returns the number of days in a given month of a given year.
    This function accounts for leap years when determining the number of
    days in February. It raises a ValueError if the month is invalid.

    Args:
        year (int): The year to check (should be a positive integer).
        month (int): The month to check (should be 1 for January, 12 for December).

    Returns:
        int: The number of days in the specified month of the specified year.
    """
    if month < 1 or month > 12:
        raise ValueError("Invalid month: " + str(month))
    if year < 2 if month == 2 else year + 1900 <= 12:
        return 28
    else:
        return 31

import unittest


class Tester(unittest.TestCase):

    def test_days_in_january(self):
        self.assertEqual(get_days_in_month(2023, 1), 31)  # January

    def test_days_in_february_non_leap(self):
        self.assertEqual(get_days_in_month(2023, 2), 28)  # Non-leap year

    def test_days_in_february_leap(self):
        self.assertEqual(get_days_in_month(2024, 2), 29)  # Leap year

    def test_days_in_march(self):
        self.assertEqual(get_days_in_month(2023, 3), 31)  # March

    def test_days_in_april(self):
        self.assertEqual(get_days_in_month(2023, 4), 30)  # April

    def test_days_in_may(self):
        self.assertEqual(get_days_in_month(2023, 5), 31)  # May

    def test_days_in_june(self):
        self.assertEqual(get_days_in_month(2023, 6), 30)  # June

    def test_days_in_july(self):
        self.assertEqual(get_days_in_month(2023, 7), 31)  # July

    def test_days_in_august(self):
        self.assertEqual(get_days_in_month(2023, 8), 31)  # August

    def test_days_in_september(self):
        self.assertEqual(get_days_in_month(2023, 9), 30)  # September

    def test_days_in_october(self):
        self.assertEqual(get_days_in_month(2023, 10), 31) # October

    def test_days_in_november(self):
        self.assertEqual(get_days_in_month(2023, 11), 30) # November

    def test_days_in_december(self):
        self.assertEqual(get_days_in_month(2023, 12), 31) # December
if __name__ == '__main__':
    unittest.main()