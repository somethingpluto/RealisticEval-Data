from datetime import timedelta
import re

def gen_timeout_timedelta(time_string: str) -> timedelta:
    pattern = r"(\d+)d?(\s*)?(\d+)h?(\s*)?(\d+)m?(\s*)?(\d+)s?(\s*)?(\d+)ms?"
    match = re.search(pattern, time_string)
    days, hours, minutes, seconds, milliseconds = map(int, match.groups())
    total_seconds = (days * 24 * 60 * 60) + (hours * 60 * 60) + (minutes * 60) + seconds + (milliseconds / 1000)
    return timedelta(seconds=total_seconds)
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