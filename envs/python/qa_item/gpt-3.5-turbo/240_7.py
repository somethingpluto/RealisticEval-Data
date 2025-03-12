from datetime import timedelta
import re

def gen_timeout_timedelta(time_string: str) -> timedelta:
    time_units = {"d": "days", "h": "hours", "m": "minutes", "s": "seconds", "ms": "milliseconds"}
    regex = r'(\d+)([dhms]+)'
    matches = re.findall(regex, time_string)

    delta_args = {}
    for match in matches:
        value = int(match[0])
        unit = match[1]
        unit_name = time_units.get(unit)
        if unit_name:
            delta_args[unit_name] = value

    return timedelta(**delta_args)
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