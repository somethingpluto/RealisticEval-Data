import unittest

class TestCalculateTotalSeconds(unittest.TestCase):

    def test_complete_time(self):
        # Test with full values provided for days, hours, minutes, and seconds
        time = [1, 2, 3, 4]  # 1 day, 2 hours, 3 minutes, 4 seconds
        expected = 93784
        result = calculate_total_seconds(time)
        self.assertEqual(result, expected)

    def test_partial_time(self):
        # Test with some values missing (assumed trailing zeros)
        time = [0, 2, 3]  # 0 days, 2 hours, 3 minutes
        expected = 7380
        result = calculate_total_seconds(time)
        self.assertEqual(result, expected)

    def test_seconds_only(self):
        # Test with only seconds provided
        time = [7200]  # 7200 seconds
        expected = 622080000
        result = calculate_total_seconds(time)
        self.assertEqual(result, expected)

    def test_no_time(self):
        # Test with no time values provided
        time = []
        expected = 0
        result = calculate_total_seconds(time)
        self.assertEqual(result, expected)