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
    # Parse the duration string
    pattern = r'P(?:(?P<years>\d+Y)?(?P<months>\d+M)?(?P<days>\d+D)?)?' \
              r'(T(?P<hours>\d+H)?(?P<minutes>\d+M)?(?P<seconds>\d+(\.\d+)?S)?)?'
    match = re.match(pattern, duration)
    if not match:
        raise ValueError("Invalid ISO 8601 duration string")

    # Extract duration components
    duration_dict = {k: int(v) if v else 0 for k, v in match.groupdict().items()}

    # Convert to a timedelta object
    delta = timedelta(**duration_dict)

    # Format the timedelta object into a human-readable string
    total_seconds = int(delta.total_seconds())
    milliseconds = int((total_seconds - int(total_seconds)) * 1000)
    seconds = total_seconds % 60
    minutes = (total_seconds // 60) % 60
    hours = (total_seconds // 3600) % 24
    days = total_seconds // 86400

    # Construct the human-readable duration string
    parts = []
    if days > 0:
        parts.append(f"{days}d")
    if hours > 0:
        parts.append(f"{hours}h")
    if minutes > 0:
        parts.append(f"{minutes}m")
    if seconds > 0:
        parts.append(f"{seconds}s")
    if milliseconds > 0:
        parts.append(f"{milliseconds}ms")

    return " ".join(parts)
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