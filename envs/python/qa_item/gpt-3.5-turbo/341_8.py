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
    if not time_str:
        raise ValueError("Input string cannot be empty")
    
    time_str = time_str.lower()  # Convert to lowercase to handle case-insensitivity
    if 'h' in time_str:
        parts = time_str.split('h')
        hours = int(parts[0])
        time_str = parts[1]
    else:
        hours = 0
    
    if 'm' in time_str:
        parts = time_str.split('m')
        minutes = int(parts[0])
        time_str = parts[1]
    else:
        minutes = 0
    
    if 's' in time_str:
        seconds = int(time_str.replace('s', ''))
    else:
        seconds = 0
    
    return (hours * 3600000) + (minutes * 60000) + (seconds * 1000)
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