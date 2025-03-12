from datetime import date, timedelta

def calculate_nth_weekday_in_month(year: int, month: int, occurrence: int, weekday: int) -> date:
    first_day = date(year, month, 1)
    days_in_month = calendar.monthrange(year, month)[1]

    if occurrence > days_in_month:
        days_to_add = occurrence - days_in_month
        next_month = month + 1
        if next_month > 12:
            year += 1
            next_month -= 1

        target_day = (days_in_month + days_to_add) % 7
        target_date = date(year, next_month, target_day)
    else:
        target_day = (weekday + occurrence - 1) % 7
        target_date = first_day + timedelta(days=target_day)

    return target_date
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