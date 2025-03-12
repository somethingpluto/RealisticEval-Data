from datetime import datetime

def convert_unix_timestamp_to_readable_date(unix_timestamp: int) -> str:
    dt = datetime.fromtimestamp(unix_timestamp)
    return dt.strftime('%b %d, %H:%M')
import unittest


class TestTimestampToReadableDate(unittest.TestCase):
    def test_convert_unix_timestamp_to_readable_format(self):
        timestamp = 1696516800
        self.assertEqual(convert_unix_timestamp_to_readable_date(timestamp), 'Oct 5, 22:40')

    def test_handle_timestamp_at_start_of_year(self):
        timestamp = 1672531200
        self.assertEqual(convert_unix_timestamp_to_readable_date(timestamp), 'Jan 1, 8:00')

    def test_handle_timestamp_at_end_of_year(self):
        timestamp = 1672531199
        self.assertEqual(convert_unix_timestamp_to_readable_date(timestamp), 'Jan 1, 7:59')

    def test_handle_timestamps_in_leap_year(self):
        timestamp = 1583020800
        self.assertEqual(convert_unix_timestamp_to_readable_date(timestamp), 'Mar 1, 8:00')

    def test_convert_timestamp_to_readable_format_with_single_digit_day(self):
        timestamp = 1675190400
        self.assertEqual(convert_unix_timestamp_to_readable_date(timestamp), 'Feb 1, 2:40')

    def test_handle_zero_unix_timestamp(self):
        timestamp = 0
        self.assertEqual(convert_unix_timestamp_to_readable_date(timestamp), 'Jan 1, 8:00')

if __name__ == '__main__':
    unittest.main()