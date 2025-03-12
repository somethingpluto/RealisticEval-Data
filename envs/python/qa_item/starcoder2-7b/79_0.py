from datetime import datetime

def generate_date_range_string(start_date: str, end_date: str) -> str:
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')

    if start.year == end.year and start.month == end.month:
        return f"{start.strftime('%B')} {start.day} to {end.day}, {start.year}"
    else:
        return f"{start.strftime('%B %d')} to {end.strftime('%B %d, %Y')}"
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