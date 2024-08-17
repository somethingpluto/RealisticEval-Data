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