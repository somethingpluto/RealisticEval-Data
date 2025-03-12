from datetime import timedelta
import re

def gen_timeout_timedelta(time_string: str) -> timedelta:
    time_units = {"d": "days", "h": "hours", "m": "minutes", "s": "seconds", "ms": "milliseconds"}
    time_pattern = re.compile(r'(\d+)([dhms]+)')
    
    total_seconds = 0
    for match in time_pattern.finditer(time_string):
        value = int(match.group(1))
        unit = match.group(2)
        unit_name = time_units.get(unit)
        
        if unit_name:
            if unit_name == "days":
                total_seconds += value * 24 * 60 * 60
            elif unit_name == "hours":
                total_seconds += value * 60 * 60
            elif unit_name == "minutes":
                total_seconds += value * 60
            elif unit_name == "seconds":
                total_seconds += value
            elif unit_name == "milliseconds":
                total_seconds += value / 1000
                
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