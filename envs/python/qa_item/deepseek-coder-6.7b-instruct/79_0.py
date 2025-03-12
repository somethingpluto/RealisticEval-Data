import datetime

def generate_date_range_string(start_date: str, end_date: str) -> str:
    """
    Generates a string based on the entered start and end dates. If the start date and end date are in the same month, only one month will be displayed. If not, the start and end months will be displayed separately.

    Args:
        start_date (str): The start date in 'YYYY-MM-DD' format.
        end_date (str): The end date in 'YYYY-MM-DD' format.

    Returns:
        str: A string representing the date range in a human-readable format.
    """
    # Convert the input strings to datetime objects
    start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    
    # Get the month names
    start_month_name = start.strftime('%B')
    end_month_name = end.strftime('%B')
    
    # Get the day and year
    start_day = start.day
    end_day = end.day
    year = start.year
    
    # Check if the start and end dates are in the same month
    if start.year == end.year and start.month == end.month:
        return f"{start_month_name} {start_day} to {end_day}, {year}"
    else:
        return f"{start_month_name} {start_day} to {end_month_name} {end_day}, {year}"
import unittest


class TestDateRangeString(unittest.TestCase):
    def test_same_month(self):
        # Test dates within the same month
        result = generate_date_range_string("2023-08-01", "2023-08-15")
        self.assertEqual(result, "August 1 to 15, 2023")

    def test_same_month_star_end(self):
        # Test dates within the same month
        result = generate_date_range_string("2023-08-01", "2023-08-31")
        self.assertEqual(result, "August 1 to 31, 2023")

    def test_different_months_same_year(self):
        # Test dates across different months within the same year
        result = generate_date_range_string("2023-08-30", "2023-09-05")
        self.assertEqual(result, "August 30, 2023 to September 5, 2023")

    def test_different_years(self):
        # Test dates across different years
        result = generate_date_range_string("2023-12-30", "2024-01-02")
        self.assertEqual(result, "December 30, 2023 to January 2, 2024")

if __name__ == '__main__':
    unittest.main()