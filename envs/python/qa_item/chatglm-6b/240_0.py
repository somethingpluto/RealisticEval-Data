
from datetime import timedelta
import re

def gen_timeout_timedelta(time_string: str) -> timedelta:
    """
    Converts a time duration string into a timedelta object.
    The input string can include days (d), hours (h), minutes (m), seconds (s), and milliseconds (ms).
    eg. "1d 2h 3m 4s 500ms"
    Each unit should be specified by an integer followed by its corresponding unit letter.

    Args:
        time_string (str): A string representing the time duration.

    Returns:
        timedelta: A timedelta object representing the input duration.
    """
    # Split the time string into individual units
    units = re.split(r'\d+', time_string)

    # Initialize the timedelta object with the current date and time
    current_date = datetime.now()
    current_time = current_date.timetuple()

    # Convert each unit into a timedelta object
    for unit in units:
        # Iterate through each unit
        for i in range(len(units)):
            # Get the unit number and unit letter
            unit_num = int(units[i])
            unit_letter = units[i][0]

            # Create a timedelta object with the current date and time and the unit number
            timedelta = current_date.replace(time=current_time, day=i, hour=0, minute=0, second=0, micros=0)

            # Add the unit to the timedelta object
            timedelta = timedelta + int(unit_num) * timedelta.days

    # Return the timedelta object
    return timedelta

import unittest
from datetime import timedelta


class TestGenTimeoutTimedelta(unittest.TestCase):
    def test_single_unit_days(self):
        self.assertEqual(gen_timeout_timedelta("5d"), timedelta(days=5))


    def test_single_unit_hours(self):
        self.assertEqual(gen_timeout_timedelta("8h"), timedelta(hours=8))

    def test_single_unit_minutes(self):
        self.assertEqual(gen_timeout_timedelta("45m"), timedelta(minutes=45))

    def test_single_unit_seconds(self):
        self.assertEqual(gen_timeout_timedelta("30s"), timedelta(seconds=30))

    def test_complex_mix(self):
        self.assertEqual(gen_timeout_timedelta("2d 20h 30m"), timedelta(days=2, hours=20, minutes=30))

    def test_no_units(self):
        self.assertEqual(gen_timeout_timedelta(""), timedelta(0))
if __name__ == '__main__':
    unittest.main()