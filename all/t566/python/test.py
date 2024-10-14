import unittest
from datetime import datetime


class TestIsSameDay(unittest.TestCase):

    def test_different_days(self):
        timestamp1 = int(datetime(2024, 10, 1, 10, 0, 0).timestamp())  # October 1, 2024, 10:00 AM UTC
        timestamp2 = int(datetime(2024, 10, 2, 10, 0, 0).timestamp())  # October 2, 2024, 10:00 AM UTC
        self.assertFalse(is_same_day(timestamp1, timestamp2))

    def test_same_day_different_times(self):
        timestamp1 = int(datetime(2024, 10, 1, 0, 0, 0).timestamp())  # October 1, 2024, 12:00 AM UTC
        timestamp2 = int(datetime(2024, 10, 1, 12, 30, 0).timestamp())  # October 1, 2024, 12:30 PM UTC
        self.assertTrue(is_same_day(timestamp1, timestamp2))

    def test_same_day_different_time_zones(self):
        timestamp1 = int(datetime(2024, 10, 1, 10, 0, 0).timestamp())  # UTC
        timestamp2 = int(datetime.fromisoformat('2024-10-01T12:00:00+02:00').timestamp())  # October 1, 2024, 12:00 PM UTC+2
        self.assertTrue(is_same_day(timestamp1, timestamp2))

    def test_midnight_same_day(self):
        timestamp1 = int(datetime(2024, 10, 1, 0, 0, 0).timestamp())  # October 1, 2024, 12:00 AM UTC
        timestamp2 = int(datetime(2024, 10, 1, 0, 0, 0).timestamp())  # Same timestamp
        self.assertTrue(is_same_day(timestamp1, timestamp2))

    def test_different_years(self):
        timestamp1 = int(datetime(2023, 10, 1, 10, 0, 0).timestamp())  # October 1, 2023, 10:00 AM UTC
        timestamp2 = int(datetime(2024, 10, 1, 10, 0, 0).timestamp())  # October 1, 2024, 10:00 AM UTC
        self.assertFalse(is_same_day(timestamp1, timestamp2))

    def test_invalid_timestamps(self):
        timestamp1 = int(datetime.fromisoformat('invalid').timestamp())  # This will raise an error, so handle it
        timestamp2 = int(datetime(2024, 10, 1, 10, 0, 0).timestamp())  # Valid timestamp
        with self.assertRaises(ValueError):
            is_same_day(timestamp1, timestamp2)
