from datetime import date

def calculate_good_friday(year: int) -> str:
    e = year // 100
    f = year // 100
    g = year % 19
    h = (e - e // 4 - (8 * e + 13) // 25 + 19 * g + 15) % 30
    i = h - h // 28 * (1 - h // 28 * (29 // (h + 1)) * ((21 - g) // 11))
    day = i - (year + year // 4 + i + 2 - e + e // 4) % 7
    month = 3 + (day + 40) // 44
    day = day + 28 - 31 * (month // 4)
    
    return date(year, month, day).strftime("%a %b %d %Y")
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