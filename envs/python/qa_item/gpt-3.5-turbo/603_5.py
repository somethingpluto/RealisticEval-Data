import datetime

def is_leap_year(year: int) -> bool:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False
import unittest


class Tester(unittest.TestCase):
    """ Test cases for the leap year function. """

    def test_divisible_by_4_but_not_by_100(self):
        """ Years that are leap years. """
        self.assertTrue(is_leap_year(2024))  # 2024 is a leap year
        self.assertTrue(is_leap_year(2000))  # 2000 is a leap year (divisible by 400)
        self.assertTrue(is_leap_year(1996))  # 1996 is a leap year
        self.assertTrue(is_leap_year(2004))  # 2004 is a leap year

    def test_divisible_by_100_but_not_by_400(self):
        """ Years that are not leap years. """
        self.assertFalse(is_leap_year(1900))  # 1900 is not a leap year
        self.assertFalse(is_leap_year(2100))  # 2100 is not a leap year
        self.assertFalse(is_leap_year(1800))  # 1800 is not a leap year

    def test_divisible_by_400(self):
        """ Years that are leap years. """
        self.assertTrue(is_leap_year(2400))  # 2400 is a leap year
        self.assertTrue(is_leap_year(1600))  # 1600 is a leap year

    def test_normal_years(self):
        """ Years that are normal years. """
        self.assertFalse(is_leap_year(1997))  # 1997 is not a leap year
        self.assertFalse(is_leap_year(1998))  # 1998 is not a leap year
        self.assertFalse(is_leap_year(1999))  # 1999 is not a leap year

if __name__ == '__main__':
    unittest.main()