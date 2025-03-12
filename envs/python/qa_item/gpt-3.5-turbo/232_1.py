from typing import Optional

def convert_hms_to_milliseconds(time_str: str) -> Optional[int]:
    hours = 0
    minutes = 0
    seconds = 0

    try:
        time_str = time_str.replace('h', ' ').replace('min', ' ').replace('s', ' ')
        time_list = time_str.split()

        if 'h' in time_str:
            hours = int(time_list[0])
        if 'min' in time_str:
            minutes = int(time_list[-2])
        if 's' in time_str:
            seconds = int(time_list[-1])

        total_milliseconds = (hours * 3600000) + (minutes * 60000) + (seconds * 1000)
        return total_milliseconds
    except ValueError:
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