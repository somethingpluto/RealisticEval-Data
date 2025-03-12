
def time_passed(start_time_in_millis: int) -> str:
    # Calculate the number of milliseconds between the start time and the current time
    current_time_in_millis = datetime.datetime.now().milliseconds
    total_milliseconds = start_time_in_millis - current_time_in_millis

    # Calculate the number of minutes and seconds between the start time and the current time
    minutes = total_milliseconds / 1000 / 60
    seconds = total_milliseconds % 1000 / 60

    # Format the elapsed time as a string in "minutes:seconds" format
    return f"{minutes:02d}:{seconds:02d}"

start_time_in_millis = 10000
elapsed_time = time_passed(start_time_in_millis)
print(elapsed_time)

1:00

import unittest
from unittest.mock import patch


class TestTimePassed(unittest.TestCase):

    @patch('time.time', return_value=1609459200)  # Mocking time to freeze at Jan 1, 2021, 00:00:00
    def test_time_passed_one_minute_ago(self, mock_time):
        start_time = 1609459140000  # 1 minute earlier
        self.assertEqual(time_passed(start_time), "1:00")

    @patch('time.time', return_value=1609459200)  # Mocking time
    def test_time_passed_boundary_59_seconds(self, mock_time):
        start_time = 1609459194100  # 59 seconds and 900 milliseconds earlier
        self.assertEqual(time_passed(start_time), "0:05")

    @patch('time.time', return_value=1609459200)  # Mocking time
    def test_time_passed_same_as_current_time(self, mock_time):
        self.assertEqual(time_passed(1609459200000), "0:00")

    @patch('time.time', return_value=1609459200)  # Mocking time
    def test_time_passed_future_start_time(self, mock_time):
        start_time = 1609459260000  # 1 minute into the future
        result = time_passed(start_time)
        self.assertRegex(result, '-')  # Expecting negative output or some error handling

    @patch('time.time', return_value=1609459200)  # Mocking time
    def test_time_passed_large_time_difference(self, mock_time):
        start_time = 1483228800000  # January 1, 2017, 00:00:00 (4 years difference)
        self.assertEqual(time_passed(start_time), "2103840:00")  # Calculated minutes for 4 years

if __name__ == '__main__':
    unittest.main()