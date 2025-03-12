
from datetime import datetime

def get_timestamp(created_at: datetime) -> str:
    """Computes the difference between the specified date and the current time, returning it in a human-readable way.
    
    Args:
        created_at (datetime): The date to calculate the time difference from.
        
    Returns:
        str: A string indicating the time elapsed, e.g., "3 days ago", "5 hours ago".
    """
    # Convert the date to a string in the format "YYYY-MM-DD"
    created_at_str = created_at.strftime("%Y-%m-%d")
    
    # Compute the time difference in hours, minutes, and seconds
    current_time = datetime.now()
    time_diff = current_time.strftime("%H:%M:%S")
    
    # Return the time difference in a human-readable format
    return f"{created_at_str} ago, {time_diff} hours, {time_diff} minutes, and {time_diff} seconds"
python
# Example usage
created_at = datetime.now() # Get the current date and time
timestamp = get_timestamp(created_at) # Compute the time difference and return it in a human-readable format
print(timestamp) # Output: "2023-03-23 10:30:00"

import unittest
from datetime import datetime, timedelta

class TestGetTimestamp(unittest.TestCase):

    def test_one_second_ago(self):
        one_second_ago = datetime.now() - timedelta(seconds=1)  # 1 second ago
        self.assertEqual(get_timestamp(one_second_ago), '1 second ago')

    def test_five_minutes_ago(self):
        five_minutes_ago = datetime.now() - timedelta(minutes=5)  # 5 minutes ago
        self.assertEqual(get_timestamp(five_minutes_ago), '5 minutes ago')

    def test_two_hours_ago(self):
        two_hours_ago = datetime.now() - timedelta(hours=2)  # 2 hours ago
        self.assertEqual(get_timestamp(two_hours_ago), '2 hours ago')

    def test_three_days_ago(self):
        three_days_ago = datetime.now() - timedelta(days=3)  # 3 days ago
        self.assertEqual(get_timestamp(three_days_ago), '3 days ago')
if __name__ == '__main__':
    unittest.main()