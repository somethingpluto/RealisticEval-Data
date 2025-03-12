from typing import List

def format_thread_count(count: int) -> str:
    """
    Formats the thread count into a user-friendly string.

    The function formats the number of threads into a two-digit string
    followed by "Thread" or "Threads" based on the count.

    For example:
        - Input: 3  Output: "03 Threads"
        - Input: 1  Output: "01 Thread"

    Args:
        count (int): The number of threads.

    Returns:
        str: A formatted string indicating the number of threads.
             The string will be in the format "XX Thread" or "XX Threads",
             where XX is the count formatted as a two-digit number.
    """
    if count == 1:
        return f"01 Thread"
    else:
        return f"{count:02d} Threads"
import unittest


class TestFormatThreadCount(unittest.TestCase):

    def test_count_of_one(self):
        """should return '01 Thread' for a count of 1"""
        self.assertEqual(format_thread_count(1), "01 Thread")

    def test_count_of_five(self):
        """should return '05 Threads' for a count of 5"""
        self.assertEqual(format_thread_count(5), "05 Threads")

    def test_count_of_ten(self):
        """should return '10 Threads' for a count of 10"""
        self.assertEqual(format_thread_count(10), "10 Threads")

    def test_count_of_ninety_nine(self):
        """should return '99 Threads' for a count of 99"""
        self.assertEqual(format_thread_count(99), "99 Threads")
if __name__ == '__main__':
    unittest.main()