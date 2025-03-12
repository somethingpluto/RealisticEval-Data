from datetime import datetime
import re

def convert_time(duration: str) -> str:
    duration = duration[2:]  # Remove the "PT" at the beginning
    readable_duration = ""

    matches = re.findall(r'(\d+\.*\d*)([A-Za-z])', duration)
    for match in matches:
        value = float(match[0])
        unit = match[1]
        if unit == 'H':
            readable_duration += f"{int(value)}h"
        elif unit == 'M':
            readable_duration += f"{int(value)}m"
        elif unit == 'S':
            seconds = value % 60
            milliseconds = (value % 1) * 1000
            readable_duration += f"{int(seconds)}s{int(milliseconds)}ms"

    return readable_duration
import unittest


class TestConvertTimeFunction(unittest.TestCase):

    def test_full_iso_duration(self):
        """Test converting full ISO 8601 duration with hours, minutes, seconds, and milliseconds."""
        self.assertEqual(convert_time('PT1H23M45.678S'), '1h23m45s678ms')

    def test_duration_with_seconds_and_milliseconds(self):
        """Test converting duration with only seconds and milliseconds."""
        self.assertEqual(convert_time('PT45.5S'), '45s500ms')

    def test_duration_with_hours_and_minutes_no_seconds(self):
        """Test converting duration with hours and minutes, but no seconds."""
        self.assertEqual(convert_time('PT2H5M'), '2h5m')

    def test_duration_with_only_seconds_no_milliseconds(self):
        """Test converting duration with only seconds, no milliseconds."""
        self.assertEqual(convert_time('PT20S'), '20s')

if __name__ == '__main__':
    unittest.main()