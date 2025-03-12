def is_break_time(start_time: str, end_time: str, current_time: str) -> bool:
    """
    Determine whether the current time is within the specified time range (i.e., whether it is a break).

    Args:
        start_time (str): The start time of the break in HH:MM format.
        end_time (str): The end time of the break in HH:MM format.
        current_time (str): The current time in HH:MM format.
    """
    start_hour, start_minute = map(int, start_time.split(':'))
    end_hour, end_minute = map(int, end_time.split(':'))
    current_hour, current_minute = map(int, current_time.split(':'))

    # Convert all times to minutes past midnight
    start_time_minutes = start_hour * 60 + start_minute
    end_time_minutes = end_hour * 60 + end_minute
    current_time_minutes = current_hour * 60 + current_minute

    # Check if current time is within the break time range
    return start_time_minutes <= current_time_minutes <= end_time_minutes
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