from datetime import datetime

def get_timestamp(created_at: datetime) -> str:
    """Computes the difference between the specified date and the current time, returning it in a human-readable way.
    
    Args:
        created_at (datetime): The date to calculate the time difference from.
        
    Returns:
        str: A string indicating the time elapsed, e.g., "3 days ago", "5 hours ago".
    """

    now = datetime.now()
    diff = now - created_at

    days = diff.days
    seconds = diff.seconds

    if days > 0:
        return f"{days} days ago"
    elif seconds < 60:
        return "Just now"
    elif seconds < 3600:
        minutes = seconds // 60
        return f"{minutes} minutes ago"
    else:
        hours = seconds // 3600
        return f"{hours} hours ago"
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