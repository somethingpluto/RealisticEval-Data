
def is_break_time(start_time: str, end_time: str, current_time: str) -> None:
    """
    Determine whether the current time is within the specified time range (i.e., whether it is a break).

    Args:
        start_time (str): The start time of the break in HH:MM format.
        end_time (str): The end time of the break in HH:MM format.
        current_time (str): The current time in HH:MM format.
    """
    # Convert the current time to a string in the specified format
    current_time_str = current_time.strftime("%H:%M")

    # Check if the start time is before the current time
    if start_time < current_time_str:
        return False

    # Check if the end time is after the current time
    if end_time > current_time_str:
        return False

    # Check if the current time is within the specified time range
    return start_time >= current_time_str and end_time <= current_time_str

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