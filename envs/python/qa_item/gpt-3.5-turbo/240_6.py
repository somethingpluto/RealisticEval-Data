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

    duration_pattern = re.compile(r'(?:(?P<days>\d+)d)? ?(?:(?P<hours>\d+)h)? ?(?:(?P<minutes>\d+)m)? ?(?:(?P<seconds>\d+)s)? ?(?:(?P<milliseconds>\d+)ms)?')

    match = duration_pattern.match(time_string)
    if match:
        days = int(match.group('days') or 0)
        hours = int(match.group('hours') or 0)
        minutes = int(match.group('minutes') or 0)
        seconds = int(match.group('seconds') or 0)
        milliseconds = int(match.group('milliseconds') or 0)

        return timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds, milliseconds=milliseconds)
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