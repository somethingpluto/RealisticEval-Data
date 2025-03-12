import datetime

def is_break_time(start_time: str, end_time: str, current_time: str) -> None:
    start_hour, start_minute = map(int, start_time.split(':'))
    end_hour, end_minute = map(int, end_time.split(':'))
    current_hour, current_minute = map(int, current_time.split(':'))
    
    start = datetime.time(start_hour, start_minute)
    end = datetime.time(end_hour, end_minute)
    current = datetime.time(current_hour, current_minute)
    
    if start <= current <= end:
        print("Current time is within the specified break time range.")
    else:
        print("Current time is not within the specified break time range.")
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