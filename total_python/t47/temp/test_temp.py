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
import datetime


def find_nth_weekday(year, month, weekday, nth):
    """
    Finds the nth occurrence of a specific weekday in a given month and year.

    Parameters:
        year (int): The year
        month (int): The month
        weekday (int): The weekday, where Monday is 0 and Sunday is 6
        nth (int): The nth occurrence of the weekday to find

    Returns:
        datetime.date: The date of the nth occurrence, or the last occurrence of the weekday if nth is not available.
    """
    # Start with the first day of the month
    first_day = datetime.date(year, month, 1)

    # Find the first occurrence of the given weekday
    first_weekday = first_day.weekday()
    if first_weekday <= weekday:
        first_occurrence = first_day + datetime.timedelta(days=(weekday - first_weekday))
    else:
        first_occurrence = first_day + datetime.timedelta(days=(7 - first_weekday + weekday))

    # Calculate the nth occurrence
    nth_occurrence = first_occurrence + datetime.timedelta(days=(nth - 1) * 7)

    # Check if the nth occurrence is within the same month
    if nth_occurrence.month == month:
        return nth_occurrence
    else:
        # If not, find the last occurrence of the weekday in the month
        # Go back one week from the first of the next month
        first_of_next_month = datetime.date(year, month + 1, 1) if month < 12 else datetime.date(year + 1, 1, 1)
        last_day_of_month = first_of_next_month - datetime.timedelta(days=1)
        last_weekday = last_day_of_month.weekday()

        if last_weekday >= weekday:
            last_occurrence = last_day_of_month - datetime.timedelta(days=(last_weekday - weekday))
        else:
            last_occurrence = last_day_of_month - datetime.timedelta(days=(7 - (weekday - last_weekday)))

        return last_occurrence