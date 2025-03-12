from typing import Optional
import re

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
    # Define the regex pattern to match the time string format
    pattern = re.compile(r'^(\d+h)?(\d+min)?(\d+s)?$')
    
    # Match the input string against the pattern
    match = pattern.match(time_str)
    
    if not match:
        return None
    
    # Extract hours, minutes, and seconds from the matched groups
    hours = match.group(1)
    minutes = match.group(2)
    seconds = match.group(3)
    
    # Initialize total milliseconds
    total_milliseconds = 0
    
    # Convert hours to milliseconds
    if hours:
        hours = int(hours[:-1])  # Remove the 'h' and convert to integer
        total_milliseconds += hours * 3600 * 1000
    
    # Convert minutes to milliseconds
    if minutes:
        minutes = int(minutes[:-3])  # Remove the 'min' and convert to integer
        total_milliseconds += minutes * 60 * 1000
    
    # Convert seconds to milliseconds
    if seconds:
        seconds = int(seconds[:-1])  # Remove the 's' and convert to integer
        total_milliseconds += seconds * 1000
    
    return total_milliseconds
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