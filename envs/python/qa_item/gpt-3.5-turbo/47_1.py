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
    # Calculate the weekday of the first day of the month
    first_day_weekday = datetime.date(year, month, 1).weekday()
    
    # Calculate the weekday of the target weekday in the first week
    target_weekday = (weekday - first_day_weekday) % 7
    
    # Calculate the number of days to add to get to the target weekday
    if target_weekday == 0:
        days_to_add = (occurrence - 1) * 7
    else:
        days_to_add = (occurrence - 1) * 7 + (7 - target_weekday)
    
    # Calculate the date of the target weekday
    target_date = datetime.date(year, month, 1) + datetime.timedelta(days=days_to_add)
    
    # Check if the target date is still within the same month
    if target_date.month != month:
        # Get the last day of the month
        last_day = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)
        
        # Find the closest previous occurrence of the weekday
        while last_day.weekday() != weekday:
            last_day -= datetime.timedelta(days=1)
        
        return last_day
    
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