def convert_time(duration: str) -> str:
    duration_parts = duration[2:].split('T')[0].split('H')
    hours = int(duration_parts[0]) if len(duration_parts) > 1 else 0

    duration_parts = duration[2:].split('T')[0].split('M')
    minutes = int(duration_parts[1]) if len(duration_parts) > 1 else 0

    duration_parts = duration[2:].split('T')[0].split('S')
    seconds = int(duration_parts[1]) if len(duration_parts) > 1 else 0

    milliseconds = 0
    if '.' in duration:
        milliseconds = int(duration.split('.')[1][:-1])

    readable_duration = ''
    if hours > 0:
        readable_duration += f'{hours}h'
    if minutes > 0:
        readable_duration += f'{minutes}m'
    if seconds > 0:
        readable_duration += f'{seconds}s'
    if milliseconds > 0:
        readable_duration += f'{milliseconds}ms'

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