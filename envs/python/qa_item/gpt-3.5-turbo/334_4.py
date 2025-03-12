from datetime import date

def calculate_good_friday(year: int) -> str:
    e = year
    a = e % 19
    b = e // 100
    c = e % 100
    d = b // 4
    f = b % 4
    g = (b + 8) // 25
    h = (b - g + 1) // 3
    i = (19 * a + b - d - h + 15) % 30
    j = c // 4
    k = c % 4
    m = (32 + 2 * e + 32 * i - h - j) % 7
    month = (i - m + 90) // 25
    day = i - m + month + 19 * (year % 19) + 15
    day -= 30 * (day // 30)
    
    if month == 3:
        return date(year, month, day).strftime("%a %b %d %Y")
    else:
        return date(year, month - 1, day + 1).strftime("%a %b %d %Y")
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