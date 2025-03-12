import re

def convert_time(duration: str) -> str:
    """
    Converts an ISO 8601 duration string into a more readable format.

    Args:
        duration (str): The ISO 8601 duration string (e.g., "PT1H23M45.678S").

    Returns:
        str: A human-readable duration string (e.g., "1h23m45s678ms").
    """
    # Regular expression to match the ISO 8601 duration format
    pattern = re.compile(r'P(?:(\d+)Y)?(?:(\d+)M)?(?:(\d+)D)?T(?:(\d+)H)?(?:(\d+)M)?(?:(\d+(?:\.\d+)?)S)?')
    match = pattern.match(duration)
    
    if not match:
        raise ValueError("Invalid ISO 8601 duration string")
    
    parts = match.groups()
    
    # Extract and format each part
    years = parts[0] if parts[0] else ""
    months = parts[1] if parts[1] else ""
    days = parts[2] if parts[2] else ""
    hours = parts[3] if parts[3] else ""
    minutes = parts[4] if parts[4] else ""
    seconds = parts[5] if parts[5] else ""
    
    # Build the human-readable string
    result = ""
    if years:
        result += f"{years}y"
    if months:
        result += f"{months}m"
    if days:
        result += f"{days}d"
    if hours:
        result += f"{hours}h"
    if minutes:
        result += f"{minutes}m"
    if seconds:
        # Split seconds and milliseconds if necessary
        if '.' in seconds:
            sec, ms = seconds.split('.')
            result += f"{sec}s{ms}ms"
        else:
            result += f"{seconds}s"
    
    return result
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