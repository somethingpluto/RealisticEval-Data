import unittest

<<<<<<< HEAD
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



import re
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
    # Regex to match hours, minutes, and seconds
    regex = r'^(?:(\d+)h)?(?:(\d+)min)?(?:(\d+)s)?$'
    match = re.search(regex, time_str)

    if not match:
        print(f'remindme.py: Cannot convert time string "{time_str}" to milliseconds!')
        return None

    # Extract hours, minutes, and seconds from the regex groups, defaulting to 0 if not present
=======

class TestConvertTimeHmsStringToMs(unittest.TestCase):
    def test_correct_conversion(self):
        # Test conversion for a correct input
        self.assertEqual(convert_time_hms_string_to_ms("2h15m30s"), (2 * 3600 + 15 * 60 + 30) * 1000)

    def test_missing_components(self):
        # Test conversion when some components are missing
        self.assertEqual(convert_time_hms_string_to_ms("45m"), 45 * 60 * 1000)
        self.assertEqual(convert_time_hms_string_to_ms("30s"), 30 * 1000)
        self.assertEqual(convert_time_hms_string_to_ms("3h"), 3 * 3600 * 1000)

    def test_no_components(self):
        # Test conversion with no valid time components
        with self.assertRaises(ValueError):
            convert_time_hms_string_to_ms("")

    def test_exceed_one_day(self):
        # Test input that exceeds one day
        with self.assertRaises(ValueError):
            convert_time_hms_string_to_ms("25h")

    def test_incorrect_format(self):
        # Test input with incorrect format
        with self.assertRaises(ValueError):
            convert_time_hms_string_to_ms("2h15m30")
import re


def convert_time_hms_string_to_ms(s):
    """
    Converts a time duration string in hours, minutes, and seconds format to milliseconds.

    Args:
    s (str): The time duration string (e.g., '2h15m30s').

    Returns:
    int: The time duration in milliseconds.

    Raises:
    ValueError: If the input string is not formatted correctly or if the time exceeds one day.
    """
    # Define the regex to parse the input string.
    if s == "":
        raise ValueError("str is empty")
    regex = r'(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?$'
    match = re.fullmatch(regex, s)

    # Check if the input is parsed correctly.
    if not match:
        raise ValueError(f"Cannot convert hms string '{s}' to ms - format is incorrect.")

    # Extract hours, minutes, and seconds from the match, defaulting to 0 if not found.
>>>>>>> main
    hours = int(match.group(1)) if match.group(1) else 0
    minutes = int(match.group(2)) if match.group(2) else 0
    seconds = int(match.group(3)) if match.group(3) else 0

<<<<<<< HEAD
    # Convert the total time to milliseconds
    milliseconds = ((hours * 60 + minutes) * 60 + seconds) * 1000

    return milliseconds
=======
    # Convert the time to milliseconds.
    ms = ((hours * 60 + minutes) * 60 + seconds) * 1000

    # Check if the calculated milliseconds exceed the number of milliseconds in one day.
    if ms > 86400000:
        raise ValueError("Total time cannot exceed one day (86400000 ms).")

    return ms
>>>>>>> main
