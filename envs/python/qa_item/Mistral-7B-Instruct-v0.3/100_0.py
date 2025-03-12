from datetime import timedelta, datetime

def convert_time(duration: str) -> str:
    """
    Converts an ISO 8601 duration string into a more readable format.

    Args:
        duration (str): The ISO 8601 duration string (e.g., "PT1H23M45.678S").

    Returns:
        str: A human-readable duration string (e.g., "1h23m45s678ms").
    """
    total_seconds = sum(int(x) for x in duration[2:].split('T')) + float(duration[-5:])
    days = total_seconds // (60 * 60 * 24)
    total_seconds %= (60 * 60 * 24)
    hours = total_seconds // (60 * 60)
    total_seconds %= (60 * 60)
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    milliseconds = int((total_seconds * 1000) % 1000)

    result = ""
    if days > 0:
        result += f"{days}d "
    if hours > 0:
        result += f"{hours}h "
    if minutes > 0:
        result += f"{minutes}m "
    if seconds > 0:
        result += f"{seconds}s "
    if milliseconds > 0:
        result += f"{milliseconds}ms"

    return result.strip()
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