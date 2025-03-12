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
    iso_duration_pattern = re.compile(r"P(?:T(?:(\d+)H)?(?:(\d+)M)?(?:(\d+\.\d+|\d+)S)?)?")
    match = iso_duration_pattern.match(duration)
    
    hours = int(match.group(1)) if match.group(1) else 0
    minutes = int(match.group(2)) if match.group(2) else 0
    seconds = float(match.group(3)) if match.group(3) else 0

    duration_obj = timedelta(hours=hours, minutes=minutes, seconds=seconds)
    milliseconds = int(duration_obj.microseconds / 1000)

    return f"{hours}h{minutes}m{int(seconds)}s{milliseconds}ms"
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