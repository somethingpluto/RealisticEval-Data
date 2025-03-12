
def extract_string_from_braces(input: str) -> str:
    """
    Extracts the string contained in the first pair of braces `{}` from the input string.

    Args:
        input (str): The input string from which the braces content will be extracted.

    Returns:
        str: A substring enclosed within the first pair of braces, or an error message if braces are missing.
    """

    start_index = input.find("{")
    if start_index == -1:
        return "Error: No opening brace found"

    end_index = input.find("}")
    if end_index == -1:
        return "Error: No closing brace found"

    return input[start_index+1:end_index]

python test_extract_string_from_braces.py

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