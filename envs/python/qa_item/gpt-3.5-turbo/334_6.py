from datetime import date

def calculate_good_friday(year: int) -> str:
    e = year // 100
    f = year // 100 + 8
    g = (c - 16) // 25
    h = (c * 100) // 100 + f - g + 1
    i = 19 * a + c - f - g + 15
    j = h // 4
    k = h % 4
    l = 32 + 2 * e + 2 * j - k - i % 30
    m = (a + 11 * h + 22 * l) // 451
    month = (l + m) // 7
    day = l + m - 7 * month

    return date(year, month, day)
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