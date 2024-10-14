import unittest


class TestIsBreakTime(unittest.TestCase):
    def test_current_time_at_start(self):
        self.assertTrue(is_break_time("09:00", "10:00", "09:00"))

    def test_current_time_within_range(self):
        self.assertTrue(is_break_time("09:00", "10:00", "09:30"))

    def test_current_time_exceeds_end_time(self):
        self.assertFalse(is_break_time("09:00", "10:00", "20:00"))

    def test_current_time_before_break_time(self):
        self.assertFalse(is_break_time("09:00", "10:00", "08:59"))

    def test_current_time_after_break_time(self):
        self.assertFalse(is_break_time("09:00", "10:00", "10:01"))
