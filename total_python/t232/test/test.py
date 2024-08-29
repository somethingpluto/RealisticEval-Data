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
>>>>>>> main
