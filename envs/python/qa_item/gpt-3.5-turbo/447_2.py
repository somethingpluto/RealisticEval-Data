from datetime import datetime
from typing import Union

def calculate_age(birth_date_string: str) -> Union[str,int]:
    """
    Calculate age based on the birth date string entered by the user.

    Input birth_date_string format such as "2000-01-01".

    Args:
        birth_date_string (str): The birth date in string format.

    Returns:
        str | int: The age as an integer or an error message as a string
                    if the date format is invalid.
    """
    try:
        birth_date = datetime.strptime(birth_date_string, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age
    except ValueError:
        return "Error: Invalid date format. Please enter date in the format 'YYYY-MM-DD'."
from datetime import datetime, timedelta
import unittest


class TestCalculateAge(unittest.TestCase):

    def test_calculates_age_correctly_for_a_birth_date_in_the_past(self):
        self.assertEqual(calculate_age('2000-01-01'), datetime.now().year - 2000)

    def test_calculates_age_correctly_for_a_birth_date_in_the_long_past(self):
        self.assertEqual(calculate_age('1000-01-01'), datetime.now().year - 1000)

    def test_calculates_age_correctly_for_a_birth_date_today(self):
        today = datetime.now().strftime('%Y-%m-%d')  # Get today's date in YYYY-MM-DD format
        self.assertEqual(calculate_age(today), 0)

    def test_calculates_age_correctly_for_a_person_born_yesterday(self):
        yesterday = datetime.now() - timedelta(days=1)  # Set to yesterday
        birth_date_string = yesterday.strftime('%Y-%m-%d')  # Format as YYYY-MM-DD
        self.assertEqual(calculate_age(birth_date_string), 0)

if __name__ == '__main__':
    unittest.main()