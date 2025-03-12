from datetime import datetime, timedelta
import re

def convert_time(duration: str) -> str:
    duration = duration.upper()
    
    # Extracting hours, minutes, seconds, and milliseconds from the duration string
    hours = int(re.search(r"T(\d+)H", duration).group(1)) if 'T' in duration else 0
    minutes = int(re.search(r"H(\d+)M", duration).group(1)) if 'H' in duration else 0
    seconds = float(re.search(r"M(\d+\.\d+S|\d+S)", duration).group(1).replace('S', '')) if 'M' in duration else 0
    
    # Converting hours, minutes, and seconds to a timedelta object
    time_delta = timedelta(hours=hours, minutes=minutes, seconds=seconds)
    
    # Formatting the time delta into a human-readable format
    formatted_time = str(time_delta).replace(':', 'h') + 'm' + str(int(seconds)) + 's' + str(int(seconds % 1 * 1000)) + 'ms'
    
    return formatted_time
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