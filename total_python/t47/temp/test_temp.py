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

# find_nth_weekday_of_specific_year_extended
from datetime import datetime, timedelta


def find_nth_weekday_of_specific_year(y, m, n, k):
    """
    Calculates the date of the nth occurrence of a specific weekday (k) in a given month (m) and year (y).
    If the nth occurrence does not exist within the month, it returns the last occurrence of that weekday in the month.
    This function extends the capability to handle edge cases where the nth weekday might not be present,
    by providing the closest previous weekday in such cases.

    Parameters:
    - y (int): The year for which the date is to be calculated.
    - m (int): The month for which the date is to be calculated, where January is 1 and December is 12.
    - n (int): The nth occurrence of the weekday within the month. For example, 1 for the first occurrence, 2 for the second, etc.
    - k (int): The weekday, where Monday is 0 and Sunday is 6.

    Returns:
    - datetime.datetime: The calculated date of the nth occurrence of the weekday in the given month and year.
      If the nth occurrence does not exist, returns the date of the last occurrence of that weekday in the month.
    """

    first_day_of_month = datetime(y, m, 1)
    day_difference = (k - first_day_of_month.weekday() + 7) % 7
    first_k_weekday_of_month = first_day_of_month + timedelta(days=day_difference)
    nth_k_weekday_of_month = first_k_weekday_of_month + timedelta(weeks=n-1)

    # その月の最終日を計算するために、次の月の第1日を取得し、1日引く
    if m == 12:
        next_month_first_day = datetime(y + 1, 1, 1)
    else:
        next_month_first_day = datetime(y, m + 1, 1)
    last_day_of_month = next_month_first_day - timedelta(days=1)

    if nth_k_weekday_of_month > last_day_of_month:
        last_k_weekday_of_month = last_day_of_month - timedelta(days=(last_day_of_month.weekday() - k + 7) % 7)
        return last_k_weekday_of_month

    return nth_k_weekday_of_month