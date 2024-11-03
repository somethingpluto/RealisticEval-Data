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