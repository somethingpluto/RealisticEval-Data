import re

def convert_time(duration: str) -> str:
    """
    Converts an ISO 8601 duration string into a more readable format.

    Args:
        duration (str): The ISO 8601 duration string (e.g., "PT1H23M45.678S").

    Returns:
        str: A human-readable duration string (e.g., "1h23m45s678ms").
    """
    
    # Regular expressions to extract hours, minutes, seconds, and milliseconds from the duration string
    hours = re.search(r"T(\d+)H", duration)
    minutes = re.search(r"H(\d+)M", duration)
    seconds = re.search(r"M(\d+\.\d+)S", duration)
    milliseconds = re.search(r"S(\d+)ms", duration)
    
    # Build the human-readable duration string
    result = ""
    if hours:
        result += hours.group(1) + "h"
    if minutes:
        result += minutes.group(1) + "m"
    if seconds:
        result += seconds.group(1).replace(".", "s")
    if milliseconds:
        result += milliseconds.group(1) + "ms"
    
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