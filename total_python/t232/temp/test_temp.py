import unittest


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
    hours = int(match.group(1)) if match.group(1) else 0
    minutes = int(match.group(2)) if match.group(2) else 0
    seconds = int(match.group(3)) if match.group(3) else 0

    # Convert the time to milliseconds.
    ms = ((hours * 60 + minutes) * 60 + seconds) * 1000

    # Check if the calculated milliseconds exceed the number of milliseconds in one day.
    if ms > 86400000:
        raise ValueError("Total time cannot exceed one day (86400000 ms).")

    return ms
