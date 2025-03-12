from datetime import datetime

def is_break_time(start_time: str, end_time: str, current_time: str) -> None:
    start = datetime.strptime(start_time, "%H:%M")
    end = datetime.strptime(end_time, "%H:%M")
    current = datetime.strptime(current_time, "%H:%M")
    
    if start <= current <= end:
        print("It is break time.")
    else:
        print("It is not break time.")
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

if __name__ == '__main__':
    unittest.main()