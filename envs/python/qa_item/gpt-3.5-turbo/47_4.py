import datetime


def calculate_nth_weekday_in_month(year: int, month: int, occurrence: int, weekday: int) -> datetime.date:
    """
    Calculates the date of the nth occurrence of a specific weekday (k) in a given month (m) and year (y).
    If the nth occurrence does not exist within the month, it returns the last occurrence of that weekday in the month.
    This function extends the capability to handle edge cases where the nth weekday might not be present,
    by providing the closest previous weekday in such cases
    Args:
        y (int): The year for which the date is to be calculated.
        m (int): The month for which the date is to be calculated, where January is 1 and December is 12.
        n (int): The nth occurrence of the weekday within the month. For example, 1 for the first occurrence, 2 for the second, etc.
        k (int): The weekday, where Monday is 0 and Sunday is 6.

    Returns:
        datetime: The calculated date of the nth occurrence of the weekday in the given month and year.
        If the nth occurrence does not exist, returns the date of the last occurrence of that weekday in the month.
    """
    # Find the first weekday in the month
    first_day = datetime.date(year, month, 1)
    while first_day.weekday() != weekday:
        first_day += datetime.timedelta(1)

    # Calculate the date of the nth occurrence of the weekday
    if occurrence == 1:
        result = first_day
    else:
        result = first_day + datetime.timedelta(7 * (occurrence - 1))

    # Check if the calculated date is still within the given month
    if result.month != month:
        result -= datetime.timedelta(7)

    return result
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