def day_of_week(year: int, month: int, day: int) -> int:
    """
    Calculates the day of the week for a given date.

    Args:
        year (int): The year of the date (e.g., 2024).
        month (int): The month of the date (1 = January, 2 = February, ..., 12 = December).
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
    if month < 3:
        month += 12
        year -= 1

    q = day
    m = month
    k = year % 100
    j = year // 100

    f = q + 13*(m+1)//5 + k + k//4 + 5*j + j//4 + 1
    return f % 7 + 1
import unittest


class Tester(unittest.TestCase):
    """Unit tests for the day_of_week function."""

    def test_day_of_week_calculation(self):
        """Test cases for day_of_week function."""
        self.assertEqual(day_of_week(2024, 1, 1), 1)  # January 1, 2024 is a Monday
        self.assertEqual(day_of_week(2023, 8, 29), 2)  # August 29, 2023 is a Tuesday
        self.assertEqual(day_of_week(2022, 12, 25), 7) # December 25, 2022 is a Sunday
        self.assertEqual(day_of_week(1989, 11, 9), 4)  # November 9, 1989 is a Thursday
        self.assertEqual(day_of_week(2000, 2, 29), 2)  # February 29, 2000 is a Tuesday
if __name__ == '__main__':
    unittest.main()