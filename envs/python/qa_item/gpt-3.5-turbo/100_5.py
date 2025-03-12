from datetime import datetime
import re

def convert_time(duration: str) -> str:
    # Define regular expressions to match different components of the duration string
    hours_pattern = re.compile(r'(\d+)H')
    minutes_pattern = re.compile(r'(\d+)M')
    seconds_pattern = re.compile(r'(\d+\.\d+)S')

    # Extract hours, minutes, and seconds from the duration string
    hours = int(hours_pattern.search(duration).group(1)) if hours_pattern.search(duration) else 0
    minutes = int(minutes_pattern.search(duration).group(1)) if minutes_pattern.search(duration) else 0
    seconds = float(seconds_pattern.search(duration).group(1)) if seconds_pattern.search(duration) else 0

    # Format the extracted components into a human-readable format
    formatted_duration = f"{hours}h{minutes}m{int(seconds)}s{int((seconds % 1) * 1000)}ms"

    return formatted_duration
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