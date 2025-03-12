from typing import Optional


def convert_hms_to_milliseconds(time_str: str) -> Optional[int]:
    """
    Convert a time duration string in the format 'XhYminZs' to milliseconds.

    This function takes a string representing a time duration, where hours, minutes, and seconds
    are optionally provided, and converts this duration into the equivalent number of milliseconds.

    Args:
        time_str (str): A string representing the time duration, e.g., '1h20min30s'.

    Returns:
        Optional[int]: The equivalent duration in milliseconds, or None if the input is invalid.
    """
    # Check if the input string is not empty
    if time_str:
        time_str = time_str.lower()
        milliseconds = 0
        hours = 0
        minutes = 0
        seconds = 0
        
        # Extract hours, minutes, and seconds from the input string
        parts = time_str.split('h')
        if len(parts) >= 2:
            try:
                hours = int(parts[0])
                time_str = parts[1]
            except ValueError:
                return None
        
        parts = time_str.split('min')
        if len(parts) >= 2:
            try:
                minutes = int(parts[0])
                time_str = parts[1]
            except ValueError:
                return None
        
        parts = time_str.split('s')
        if len(parts) >= 2:
            try:
                seconds = int(parts[0])
            except ValueError:
                return None
        
        # Convert hours, minutes, and seconds to milliseconds
        milliseconds = (hours * 3600000) + (minutes * 60000) + (seconds * 1000)
        return milliseconds
    
    return None
import unittest

class TestConvertHmsToMilliseconds(unittest.TestCase):

    def test_basic_conversion(self):
        self.assertEqual(convert_hms_to_milliseconds("1h20min30s"), 4830000, "Should convert 1h20min30s to 4830000 milliseconds")

    def test_no_hours_or_minutes(self):
        self.assertEqual(convert_hms_to_milliseconds("30s"), 30000, "Should convert 30s to 30000 milliseconds")

    def test_invalid_format(self):
        self.assertIsNone(convert_hms_to_milliseconds("1hour20minutes"), "Should return None for invalid time format")

    def test_edge_case_max_one_day(self):
        self.assertEqual(convert_hms_to_milliseconds("23h59min59s"), 86399000, "Should convert 23h59min59s to 86399000 milliseconds")

    def test_exceeding_one_day(self):
        self.assertEqual(convert_hms_to_milliseconds("24h1min"), 86460000,
                         "Should correctly convert 24h1min to 86460000 milliseconds")
if __name__ == '__main__':
    unittest.main()