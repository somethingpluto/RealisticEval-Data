from typing import Optional

def convert_hms_to_milliseconds(time_str: str) -> Optional[int]:
    parts = time_str.split()
    milliseconds = 0

    for part in parts:
        if 'h' in part:
            hours = int(part.replace('h', ''))
            milliseconds += hours * 60 * 60 * 1000
        elif 'min' in part:
            minutes = int(part.replace('min', ''))
            milliseconds += minutes * 60 * 1000
        elif 's' in part:
            seconds = int(part.replace('s', ''))
            milliseconds += seconds * 1000
        else:
            return None  # Invalid input

    return milliseconds
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