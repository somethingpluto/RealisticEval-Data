
def calculate_age(birth_date_string: str) -> str:
    """
    Calculates the age from the given birth date string and returns a string containing
    the original birth date and the calculated age. If the entered date string is invalid
    or empty, the function returns an empty string.

    Args:
        birth_date_string (str): The birth date as a string in a recognizable date format
                                  (e.g., 'YYYY-MM-DD').

    Returns:
        str: A string that includes the original birth date and the calculated age in the
             format 'birth_date_string (age)', or an empty string if the input is invalid.
    """
    if not birth_date_string or birth_date_string.isdigit():
        return ""
    else:
        year = int(birth_date_string[:4])
        month = int(birth_date_string[5:7])
        day = int(birth_date_string[8:10])
        age = year * 100 + month * 10 + day
        return "{:02d} {:02d}".format(year, age)

import unittest


class TestCalculateAge(unittest.TestCase):

    def test_birthday_today(self):
        self.assertEqual(calculate_age('2000-08-23'), '2000-08-23 (24)')

    def test_birthday_passed_this_year(self):
        self.assertEqual(calculate_age('1990-01-15'), '1990-01-15 (34)')

    def test_birthday_at_end_of_year(self):
        self.assertEqual(calculate_age('1985-12-31'), '1985-12-31 (38)')

    def test_recently_turned_one_year_old(self):
        self.assertEqual(calculate_age('2023-05-05'), '2023-05-05 (1)')

    def test_invalid_date_input(self):
        self.assertEqual(calculate_age('invalid-date'), '')

if __name__ == '__main__':
    unittest.main()