from datetime import date, timedelta

def calculate_good_friday(year: int) -> str:
    """
    Calculate the date of Good Friday in a given year.

    For example:
        input: 2024
        output: Fri Mar 29 2024

    Args:
        year (int): The year for which to calculate Good Friday.

    Returns:
        str: The date of Good Friday.
    """
    # Calculate the date of Easter
    a = year % 19
    b = year // 100
    c = year % 100
    d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
    e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
    f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
    month = f // 31
    day = f % 31 + 1

    # Calculate Good Friday, which is 2 days before Easter
    good_friday = date(year, month, day) - timedelta(days=2)

    # Return the date in the specified format
    return good_friday.strftime('%a %b %d %Y')
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