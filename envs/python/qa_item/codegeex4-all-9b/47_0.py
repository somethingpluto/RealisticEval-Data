from datetime import datetime, timedelta

def calculate_nth_weekday_in_month(year: int, month: int, occurrence: int, weekday: int) -> datetime.date:
    # Initialize the first day of the month
    first_day = datetime(year, month, 1)
    
    # Calculate the difference between the first day of the month and the target weekday
    delta_days = (weekday - first_day.weekday() + 7) % 7
    
    # Calculate the date of the first occurrence of the target weekday
    first_target_day = first_day + timedelta(days=delta_days)
    
    # Calculate the date of the nth occurrence of the target weekday
    nth_target_day = first_target_day + timedelta(weeks=occurrence-1)
    
    # If the nth occurrence is in the next month, return the last occurrence of the target weekday in the current month
    if nth_target_day.month != month:
        last_day_of_month = datetime(year, month, 1) + timedelta(days=32-month)
        return last_day_of_month - timedelta(days=last_day_of_month.weekday() - weekday)
    
    return nth_target_day.date()
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