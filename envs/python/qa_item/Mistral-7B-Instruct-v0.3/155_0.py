from datetime import datetime, timedelta

def get_timestamp(created_at: datetime) -> str:
    now = datetime.now()
    diff = now - created_at

    if diff.days > 0:
        return f"{abs(diff.days)} days ago"
    elif diff.seconds > 60:
        minutes = diff.seconds // 60
        if minutes >= 60:
            hours = minutes // 60
            return f"{hours} hours ago" if hours > 1 else f"1 hour ago"
        return f"{minutes} minutes ago"
    elif diff.seconds > 0:
        return f"{diff.seconds} seconds ago"
    else:
        return "Just now"
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