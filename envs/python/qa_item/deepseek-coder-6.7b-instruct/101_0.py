def is_break_time(start_time: str, end_time: str, current_time: str) -> None:
    """
    Determine whether the current time is within the specified time range (i.e., whether it is a break).

    Args:
        start_time (str): The start time of the break in HH:MM format.
        end_time (str): The end time of the break in HH:MM format.
        current_time (str): The current time in HH:MM format.
    """
    from datetime import datetime

    # Convert the time strings to datetime objects
    start = datetime.strptime(start_time, "%H:%M")
    end = datetime.strptime(end_time, "%H:%M")
    current = datetime.strptime(current_time, "%H:%M")

    # Check if the current time is within the break period
    if start <= end:
        # Normal case: start time is before or equal to end time
        is_break = start <= current <= end
    else:
        # Special case: start time is after end time (e.g., break spans midnight)
        is_break = start <= current or current <= end

    # Print the result
    if is_break:
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