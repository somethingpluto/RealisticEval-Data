import unittest

class TestGenTimeoutTimedelta(unittest.TestCase):

    def test_complete_time_string(self):
        """ Test a string containing all time units """
        result = gen_timeout_timedelta("1d 2h 3m 4s 500ms")
        self.assertEqual(result.days, 1)
        self.assertEqual(result.seconds, (2 * 3600) + (3 * 60) + 4)
        self.assertEqual(result.microseconds, 500000)

    def test_partial_time_string(self):
        """ Test a string containing only some time units """
        result = gen_timeout_timedelta("2h 30m")
        self.assertEqual(result.days, 0)
        self.assertEqual(result.seconds, (2 * 3600) + (30 * 60))
        self.assertEqual(result.microseconds, 0)

    def test_empty_time_string(self):
        """ Test an empty string which should raise ValueError """
        with self.assertRaises(ValueError):
            gen_timeout_timedelta("")

    def test_incorrect_format(self):
        """ Test a string with an incorrect format """
        with self.assertRaises(ValueError):
            gen_timeout_timedelta("5 days 4 hours")

    def test_no_time_units(self):
        """ Test a string that specifies numbers but no units """
        with self.assertRaises(ValueError):
            gen_timeout_timedelta("1 2 3 4 5")
import re
from datetime import timedelta


def gen_timeout_timedelta(time_string):
    """
    Converts a time duration string into a timedelta object.

    The input string can include days (d), hours (h), minutes (m), seconds (s), and milliseconds (ms).
    Each unit should be specified by an integer followed by its corresponding unit letter.

    Args:
    time_string (str): A string representing the time duration.

    Returns:
    timedelta: A timedelta object representing the input duration.

    Raises:
    ValueError: If the input string is in an incorrect format.
    """
    # Regex pattern to extract days, hours, minutes, seconds, and milliseconds
    if time_string == "":
        raise ValueError("empty time str")
    pattern = r'(?:(\d+)\s*d)?\s*(?:(\d+)\s*h)?\s*(?:(\d+)\s*m)?\s*(?:(\d+)\s*s)?\s*(?:(\d+)\s*ms)?'
    matches = re.fullmatch(pattern, time_string.strip())

    if not matches:
        raise ValueError("Invalid time format")

    # Extracting time units from the match groups, defaulting to 0 if not present
    days, hours, minutes, seconds, milliseconds = (int(x) if x else 0 for x in matches.groups())

    # Creating a timedelta object from the extracted values
    return timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds, milliseconds=milliseconds)