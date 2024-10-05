import unittest
from datetime import timedelta


class TestGenTimeoutTimedelta(unittest.TestCase):
    def test_single_unit_days(self):
        self.assertEqual(gen_timeout_timedelta("5d"), timedelta(days=5))

    def test_multiple_units(self):
        self.assertEqual(gen_timeout_timedelta("1d 2h 3m 4s 500ms"),
                         timedelta(days=1, hours=2, minutes=3, seconds=4, milliseconds=500))

    def test_single_unit_hours(self):
        self.assertEqual(gen_timeout_timedelta("8h"), timedelta(hours=8))

    def test_single_unit_minutes(self):
        self.assertEqual(gen_timeout_timedelta("45m"), timedelta(minutes=45))

    def test_single_unit_seconds(self):
        self.assertEqual(gen_timeout_timedelta("30s"), timedelta(seconds=30))

    def test_complex_mix(self):
        self.assertEqual(gen_timeout_timedelta("2d 20h 30m"), timedelta(days=2, hours=20, minutes=30))

    def test_no_units(self):
        self.assertEqual(gen_timeout_timedelta(""), timedelta(0))
