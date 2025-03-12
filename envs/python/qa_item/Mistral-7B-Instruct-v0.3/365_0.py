from datetime import date

def day_of_week(year: int, month: int, day: int) -> int:
    return date(year, month, day).weekday() + 1
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