import unittest
from datetime import datetime


class TestFindNthWeekdayOfSpecificYear(unittest.TestCase):

    def test_regular_occurrence(self):
        # Test for the 2nd Monday of May 2023
        result = find_nth_weekday_of_specific_year(2023, 5, 2, 0)
        expected = datetime(2023, 5, 8)
        self.assertEqual(result, expected)

    def test_last_occurrence(self):
        # Test for the 5th Monday of May 2023, which doesn't exist, should return the last Monday
        result = find_nth_weekday_of_specific_year(2023, 5, 5, 0)
        expected = datetime(2023, 5, 29)
        self.assertEqual(result, expected)

    def test_out_of_range(self):
        # Test for the 10th Monday of May 2023, which definitely doesn't exist, should return the last Monday
        result = find_nth_weekday_of_specific_year(2023, 5, 10, 0)
        expected = datetime(2023, 5, 29)
        self.assertEqual(result, expected)

    def test_first_day_is_weekday(self):
        # Test for when the first day of the month is the weekday in question, 1st Tuesday of August 2023
        result = find_nth_weekday_of_specific_year(2023, 8, 1, 1)
        expected = datetime(2023, 8, 1)
        self.assertEqual(result, expected)

    def test_edge_year_transition(self):
        # Test for the 1st Friday of December 2023, checking the transition to a new year boundary condition
        result = find_nth_weekday_of_specific_year(2023, 12, 1, 4)
        expected = datetime(2023, 12, 1)
        self.assertEqual(result, expected)