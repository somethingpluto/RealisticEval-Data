import unittest
import datetime

class TestFindNthWeekday(unittest.TestCase):
    def test_fifth_monday_of_march_2023(self):
        result = find_nth_weekday(2023, 3, 0, 5)
        self.assertEqual(result, datetime.date(2023, 3, 27))

    def test_fifth_friday_of_february_2024(self):
        # February 2024 has 5 Fridays
        result = find_nth_weekday(2024, 2, 4, 5)
        self.assertEqual(result, datetime.date(2024, 2, 29))

    def test_fourth_sunday_of_february_2023(self):
        # February 2023 has only 4 Sundays
        result = find_nth_weekday(2023, 2, 6, 4)
        self.assertEqual(result, datetime.date(2023, 2, 26))

    def test_sixth_tuesday_of_june_2023(self):
        # June 2023 does not have a sixth Tuesday, should return the last one
        result = find_nth_weekday(2023, 6, 1, 6)
        self.assertEqual(result, datetime.date(2023, 6, 27))

    def test_first_wednesday_of_april_2022(self):
        # Testing for the first Wednesday
        result = find_nth_weekday(2022, 4, 2, 1)
        self.assertEqual(result, datetime.date(2022, 4, 6))