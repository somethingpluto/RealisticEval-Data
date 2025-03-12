
def day_of_week(year: int, month: int, day: int) -> int:
    """Calculates the day of the week for a given date.

    Args:
        year (int): The year of the date (e.g., 2024).
        month (int): The month of the date (1 = January, 2 = February,..., 12 = December).
        day (int): The day of the month (1 to 31, depending on the month).

    Returns:
        int: An integer representing the day of the week:
            - 1 for Monday
            - 2 for Tuesday
            - 3 for Wednesday
            - 4 for Thursday
            - 5 for Friday
            - 6 for Saturday
            - 7 for Sunday
    """
    if month == 1:
        if day > 31:
            return 1
        else:
            return day - 31
    elif month == 2:
        if day > 30:
            return 2
        else:
            return day - 30
    elif month == 3:
        if day > 28:
            return 3
        else:
            return day - 28
    elif month == 4:
        if day > 27:
            return 4
        else:
            return day - 27
    elif month == 5:
        if day > 26:
            return 5
        else:
            return day - 26
    elif month == 6:
        if day > 25:
            return 6
        else:
            return day - 25
    elif month == 7:
        if day > 24:
            return 7
        else:
            return day - 24
    else:
        return 0
python
date = datetime.date(2024, 1, 1)
day_of_week_result = day_of_week(date.year, date.month, date.day)
print(day_of_week_result)  # Output: 1

import unittest


class Tester(unittest.TestCase):
    """Unit tests for the day_of_week function."""

    def test_day_of_week_2024(self):
        """Test case for January 1, 2024."""
        self.assertEqual(day_of_week(2024, 1, 1), 1)  # January 1, 2024 is a Monday

    def test_day_of_week_2023(self):
        """Test case for August 29, 2023."""
        self.assertEqual(day_of_week(2023, 8, 29), 2)  # August 29, 2023 is a Tuesday

    def test_day_of_week_2022(self):
        """Test case for December 25, 2022."""
        self.assertEqual(day_of_week(2022, 12, 25), 7) # December 25, 2022 is a Sunday

    def test_day_of_week_1989(self):
        """Test case for November 9, 1989."""
        self.assertEqual(day_of_week(1989, 11, 9), 4)  # November 9, 1989 is a Thursday

    def test_day_of_week_2000(self):
        """Test case for February 29, 2000."""
        self.assertEqual(day_of_week(2000, 2, 29), 2)  # February 29, 2000 is a Tuesday
if __name__ == '__main__':
    unittest.main()