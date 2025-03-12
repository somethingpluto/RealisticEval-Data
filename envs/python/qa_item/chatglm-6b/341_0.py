
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
    try:
        # Parse the time string into hours, minutes, and seconds
        hours, minutes, seconds = map(int, time_str.split("h"))

        # Convert the time string to hms format
        hms_str = "{:02d}h{:02d}m{:02d}s".format(hours, minutes, seconds)

        # Convert the hms string to milliseconds
        ms = hms_str.split("s")[1].split(" ")[0] * 1000
        return ms
    except ValueError as e:
        print(f"Error: {e}")
        return -1

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