from typing import List

def convert_time_hms_string_to_ms(time_str: str) -> int:
    """
    Converts a time string in the format "XhYmZs" (hours, minutes, seconds) into milliseconds.

    Args:
        time_str (str): The input string representing the time duration.

    Returns:
        int: The time in milliseconds.

    Raises:
        ValueError: If the input string does not match the expected format.
    """
    if not isinstance(time_str, str):
        raise ValueError("Input must be a string")

    if 'h' not in time_str or 'm' not in time_str or 's' not in time_str:
        raise ValueError("Input string does not match expected format")

    time_components = time_str.split('h')
    if len(time_components) != 2:
        raise ValueError("Input string does not match expected format")

    hours = int(time_components[0])

    time_components = time_components[1].split('m')
    if len(time_components) != 2:
        raise ValueError("Input string does not match expected format")

    minutes = int(time_components[0])

    time_components = time_components[1].split('s')
    if len(time_components) != 2:
        raise ValueError("Input string does not match expected format")

    seconds = int(time_components[0])

    milliseconds = (hours * 60 * 60 * 1000) + (minutes * 60 * 1000) + (seconds * 1000)

    return milliseconds
import unittest


class TestConvertTimeHmsStringToMs(unittest.TestCase):

    def test_converts_typical_time_string_correctly(self):
        result = convert_time_hms_string_to_ms('1h30m15s')
        self.assertEqual(result, 5415000)  # 1 hour + 30 minutes + 15 seconds in ms

    def test_correctly_converts_string_with_zero_values(self):
        result = convert_time_hms_string_to_ms('0h0m0s')
        self.assertEqual(result, 0)  # 0 ms

    def test_converts_maximum_single_digit_values(self):
        result = convert_time_hms_string_to_ms('9h59m59s')
        self.assertEqual(result, 35999000)  # 9 hours + 59 minutes + 59 seconds in ms

    def test_handles_large_values(self):
        result = convert_time_hms_string_to_ms('100h0m0s')
        self.assertEqual(result, 360000000)  # 100 hours in ms

    def test_correctly_converts_strings_with_leading_zeros(self):
        result = convert_time_hms_string_to_ms('01h01m01s')
        self.assertEqual(result, 3661000)  # 1 hour + 1 minute + 1 second in ms

if __name__ == '__main__':
    unittest.main()