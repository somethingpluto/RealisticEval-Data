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
