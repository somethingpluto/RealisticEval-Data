import unittest
from datetime import timedelta


class TestGenTimeoutTimedelta(unittest.TestCase):

    def test_complete_time_string(self):
        """ Test a string containing all time units """
        result = gen_timeout_timedelta("1d 2h 3m 4s 500ms")
        self.assertEqual(result.days, 1)
        self.assertEqual(result.seconds, (2 * 3600) + (3 * 60) + 4)
        self.assertEqual(result.microseconds, 500000)

    def test_partial_time_string(self):
        """ Test a string containing only some time units """
        result = gen_timeout_timedelta("2h 30m")
        self.assertEqual(result.days, 0)
        self.assertEqual(result.seconds, (2 * 3600) + (30 * 60))
        self.assertEqual(result.microseconds, 0)

    def test_empty_time_string(self):
        """ Test an empty string which should raise ValueError """
        with self.assertRaises(ValueError):
            gen_timeout_timedelta("")

    def test_incorrect_format(self):
        """ Test a string with an incorrect format """
        with self.assertRaises(ValueError):
            gen_timeout_timedelta("5 days 4 hours")

    def test_no_time_units(self):
        """ Test a string that specifies numbers but no units """
        with self.assertRaises(ValueError):
            gen_timeout_timedelta("1 2 3 4 5")