from datetime import date, timedelta

def calculate_good_friday(year: int) -> date:
    """
    Calculate the date of Good Friday in a given year.

    Args:
        year (int): The year for which to calculate Good Friday.

    Returns:
        date: The date of Good Friday.
    """
    easter_date = date(year, 3, 21) + timedelta(easter_days)
    good_friday_date = easter_date - timedelta(days=2)
    return good_friday_date
import unittest


class TestCalculateGoodFriday(unittest.TestCase):

    def test_calculate_good_friday_2024(self):
        result = calculate_good_friday(2024)
        self.assertEqual(result.strftime('%a %b %d %Y'), 'Fri Mar 29 2024')

    def test_calculate_good_friday_2021(self):
        result = calculate_good_friday(2021)
        self.assertEqual(result.strftime('%a %b %d %Y'), 'Fri Apr 02 2021')

    def test_calculate_good_friday_2000(self):
        result = calculate_good_friday(2000)
        self.assertEqual(result.strftime('%a %b %d %Y'), 'Fri Apr 21 2000')

    def test_calculate_good_friday_2019(self):
        result = calculate_good_friday(2019)
        self.assertEqual(result.strftime('%a %b %d %Y'), 'Fri Apr 19 2019')

    def test_calculate_good_friday_1999(self):
        result = calculate_good_friday(1999)
        self.assertEqual(result.strftime('%a %b %d %Y'), 'Fri Apr 02 1999')

    def test_calculate_good_friday_1981(self):
        result = calculate_good_friday(1981)
        self.assertEqual(result.strftime('%a %b %d %Y'), 'Fri Apr 17 1981')

    def test_calculate_good_friday_1954(self):
        result = calculate_good_friday(1954)
        self.assertEqual(result.strftime('%a %b %d %Y'), 'Fri Apr 16 1954')

if __name__ == '__main__':
    unittest.main()