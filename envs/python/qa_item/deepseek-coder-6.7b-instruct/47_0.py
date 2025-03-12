import datetime

def calculate_nth_weekday_in_month(year: int, month: int, occurrence: int, weekday: int) -> datetime.date:
    """
    Calculates the date of the nth occurrence of a specific weekday (k) in a given month (m) and year (y).
    If the nth occurrence does not exist within the month, it returns the last occurrence of that weekday in the month.
    
    Args:
        year (int): The year for which the date is to be calculated.
        month (int): The month for which the date is to be calculated, where January is 1 and December is 12.
        occurrence (int): The nth occurrence of the weekday within the month. For example, 1 for the first occurrence, 2 for the second, etc.
        weekday (int): The weekday, where Monday is 0 and Sunday is 6.

    Returns:
        datetime.date: The calculated date of the nth occurrence of the weekday in the given month and year.
        If the nth occurrence does not exist, returns the date of the last occurrence of that weekday in the month.
    """
    # Get the first day of the month
    first_day_of_month = datetime.date(year, month, 1)
    
    # Calculate the first occurrence of the desired weekday in the month
    if first_day_of_month.weekday() <= weekday:
        first_occurrence = first_day_of_month + datetime.timedelta(days=(weekday - first_day_of_month.weekday()))
    else:
        first_occurrence = first_day_of_month + datetime.timedelta(days=(7 + weekday - first_day_of_month.weekday()))
    
    # Calculate the nth occurrence
    nth_occurrence = first_occurrence + datetime.timedelta(weeks=(occurrence - 1))
    
    # Check if the nth occurrence is still within the same month
    if nth_occurrence.month == month:
        return nth_occurrence
    else:
        # If not, return the last occurrence of the weekday in the month
        last_day_of_month = datetime.date(year, month, 1) + datetime.timedelta(days=32)
        last_day_of_month = last_day_of_month.replace(day=1) - datetime.timedelta(days=1)
        
        # Find the last occurrence of the desired weekday in the month
        if last_day_of_month.weekday() >= weekday:
            last_occurrence = last_day_of_month - datetime.timedelta(days=(last_day_of_month.weekday() - weekday))
        else:
            last_occurrence = last_day_of_month - datetime.timedelta(days=(7 + last_day_of_month.weekday() - weekday))
        
        return last_occurrence
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