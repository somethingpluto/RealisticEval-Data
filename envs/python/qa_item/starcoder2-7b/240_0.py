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
    # Define the regular expression pattern
    pattern = r'(\d+)([dDhHmMsS])'

    # Find all matches in the string
    matches = re.findall(pattern, time_string)

    # Initialize the total timedelta
    total_timedelta = timedelta(0)

    # Loop over all matches
    for match in matches:
        # Extract the number and unit from the match
        number, unit = match
        number = int(number)
        unit = unit.lower()

        # Convert the unit to seconds
        if unit == 'd':
            number *= 24 * 60 * 60  # convert days to seconds
        elif unit == 'h':
            number *= 60 * 60  # convert hours to seconds
        elif unit == 'm':
            number *= 60  # convert minutes to seconds
        elif unit == 's':
            pass  # seconds stay the same
        elif unit == 'ms':
            number /= 1000  # convert milliseconds to seconds
        else:
            raise ValueError(f'Invalid unit: {unit}')

        # Add the timedelta to the total
        total_timedelta += timedelta(seconds=number)

    return total_timedelta
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