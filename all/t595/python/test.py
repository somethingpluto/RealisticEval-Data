import unittest


class Tester(unittest.TestCase):

    def test_get_days_in_month(self):
        # Regular months
        self.assertEqual(get_days_in_month(2023, 1), 31)  # January
        self.assertEqual(get_days_in_month(2023, 3), 31)  # March
        self.assertEqual(get_days_in_month(2023, 4), 30)  # April
        self.assertEqual(get_days_in_month(2023, 5), 31)  # May
        self.assertEqual(get_days_in_month(2023, 6), 30)  # June
        self.assertEqual(get_days_in_month(2023, 7), 31)  # July
        self.assertEqual(get_days_in_month(2023, 8), 31)  # August
        self.assertEqual(get_days_in_month(2023, 9), 30)  # September
        self.assertEqual(get_days_in_month(2023, 10), 31) # October
        self.assertEqual(get_days_in_month(2023, 11), 30) # November
        self.assertEqual(get_days_in_month(2023, 12), 31) # December

        # February in leap year
        self.assertEqual(get_days_in_month(2024, 2), 29)  # Leap year

        # February in non-leap year
        self.assertEqual(get_days_in_month(2023, 2), 28)  # Non-leap year