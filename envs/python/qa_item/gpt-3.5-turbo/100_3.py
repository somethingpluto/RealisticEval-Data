from datetime import timedelta
import re

def convert_time(duration: str) -> str:
    """
    Converts an ISO 8601 duration string into a more readable format.

    Args:
        duration (str): The ISO 8601 duration string (e.g., "PT1H23M45.678S").

    Returns:
        str: A human-readable duration string (e.g., "1h23m45s678ms").
    """
    time_pattern = re.compile(r'(\d+)([A-Za-z]+)')

    conversions = {
        'Y': timedelta(days=365),
        'M': timedelta(days=30),
        'W': timedelta(weeks=1),
        'D': timedelta(days=1),
        'H': timedelta(hours=1),
        'M': timedelta(minutes=1),
        'S': timedelta(seconds=1),
        'ms': timedelta(milliseconds=1),
        'us': timedelta(microseconds=1)
    }

    total_duration = timedelta()
    for amount, unit in time_pattern.findall(duration):
        total_duration += int(amount) * conversions[unit]

    readable_duration = str(total_duration).lower().replace(' ', '').replace(':', 'h').replace('.', 's')

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