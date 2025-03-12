def format_thread_count(count: int) -> str:
    formatted_count = str(count).zfill(2)
    if count == 1:
        return f"{formatted_count} Thread"
    else:
        return f"{formatted_count} Threads"
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