import datetime

def calculate_nth_weekday_in_month(year: int, month: int, occurrence: int, weekday: int) -> datetime.date:
    weekday = min(weekday, 6)  # Ensure weekday is within 0-6 range
    if occurrence < 1 or occurrence > 5:  # Ensure occurrence is within 1-5 range
        raise ValueError("Occurrence should be between 1 and 5")

    # Find the first weekday of the month
    first_day_of_month = datetime.date(year, month, 1)
    first_weekday = (weekday - first_day_of_month.weekday()) % 7
    if first_weekday == 0:
        first_weekday = 7

    # Calculate the date of the nth occurrence of the weekday in the month
    target_day = first_weekday + (occurrence - 1) * 7
    if target_day > 31:
        return datetime.date(year, month, 31)
    return datetime.date(year, month, target_day)
import unittest
import datetime


class TestFindNthWeekdayOfSpecificYear(unittest.TestCase):

    def test_regular_occurrence(self):
        # Test for the 2nd Monday of May 2023
        result = calculate_nth_weekday_in_month(2023, 5, 2, 0)  # Monday is 0
        expected = datetime.date(2023, 5, 8)
        self.assertEqual(result, expected)

    def test_last_occurrence(self):
        # Test for the 5th Monday of May 2023, which doesn't exist, should return the last Monday
        result = calculate_nth_weekday_in_month(2023, 5, 5, 0)  # Monday is 0
        expected = datetime.date(2023, 5, 29)
        self.assertEqual(result, expected)

    def test_first_day_is_weekday(self):
        # Test for when the first day of the month is the weekday in question, 1st Tuesday of August 2023
        result = calculate_nth_weekday_in_month(2023, 8, 1, 1)  # Tuesday is 1
        expected = datetime.date(2023, 8, 1)
        self.assertEqual(result, expected)

    def test_edge_year_transition(self):
        # Test for the 1st Friday of December 2023
        result = calculate_nth_weekday_in_month(2023, 12, 1, 4)  # Friday is 4
        expected = datetime.date(2023, 12, 1)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()