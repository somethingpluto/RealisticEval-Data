from datetime import timedelta
import re

def gen_timeout_timedelta(time_string: str) -> timedelta:
    units = {
        'd': 'days',
        'h': 'hours',
        'm': 'minutes',
        's': 'seconds',
        'ms': 'milliseconds'
    }
    
    duration = 0
    for match in re.finditer(r'(\d+)([dhms]{1,2})', time_string):
        value = int(match.group(1))
        unit = units.get(match.group(2))
        
        if unit:
            if unit == 'days':
                duration += timedelta(days=value)
            elif unit == 'hours':
                duration += timedelta(hours=value)
            elif unit == 'minutes':
                duration += timedelta(minutes=value)
            elif unit == 'seconds':
                duration += timedelta(seconds=value)
            elif unit == 'milliseconds':
                duration += timedelta(milliseconds=value)
    
    return duration
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