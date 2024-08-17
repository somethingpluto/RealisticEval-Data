import unittest

class TestDateRangeString(unittest.TestCase):
    def test_same_month(self):
        # Test dates within the same month
        result = date_range_string("2023-08-01", "2023-08-15")
        self.assertEqual(result, "August 1 to 15, 2023")

    def test_different_months_same_year(self):
        # Test dates across different months within the same year
        result = date_range_string("2023-08-30", "2023-09-05")
        self.assertEqual(result, "August 30 to September 5, 2023")

    def test_different_years(self):
        # Test dates across different years
        result = date_range_string("2023-12-30", "2024-01-02")
        self.assertEqual(result, "December 30, 2023 to January 2, 2024")

    def test_incorrect_date_format(self):
        # Test incorrect date formats
        with self.assertRaises(ValueError) as context:
            date_range_string("2023/08/01", "2023/08/15")
        self.assertTrue("Date must be in 'YYYY-MM-DD' format." in str(context.exception))

    def test_start_date_after_end_date(self):
        # Test logical error where start date is after end date
        with self.assertRaises(ValueError) as context:
            date_range_string("2023-08-15", "2023-08-01")
        self.assertTrue("start_date cannot be after end_date." in str(context.exception))
from datetime import datetime


def date_range_string(start_date: str, end_date: str) -> str:
    """
    Generate a formatted date range string.

    Args:
    start_date (str): The start date in 'YYYY-MM-DD' format.
    end_date (str): The end date in 'YYYY-MM-DD' format.

    Returns:
    str: A string representing the date range in a human-readable format.

    Raises:
    ValueError: If the start_date or end_date are not in the correct format or if start_date is after end_date.
    """
    try:
        start_dt = datetime.strptime(start_date, '%Y-%m-%d')
        end_dt = datetime.strptime(end_date, '%Y-%m-%d')

        if start_dt > end_dt:
            raise ValueError("start_date cannot be after end_date.")
    except ValueError as e:
        raise ValueError(f"Date must be in 'YYYY-MM-DD' format. {e}")

    start_month = start_dt.strftime('%B')
    end_month = end_dt.strftime('%B')
    start_day = str(start_dt.day)
    end_day = str(end_dt.day)
    start_year = str(start_dt.year)
    end_year = str(end_dt.year)

    # Format output based on whether dates are within the same month and/or year
    if start_year != end_year:
        return f"{start_month} {start_day}, {start_year} to {end_month} {end_day}, {end_year}"
    elif start_month == end_month:
        return f"{start_month} {start_day} to {end_day}, {start_year}"
    else:
        return f"{start_month} {start_day} to {end_month} {end_day}, {start_year}"
