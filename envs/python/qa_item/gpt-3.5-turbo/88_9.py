from croniter import croniter
from datetime import datetime

def is_cron_between_2_and_4_am(cron_expression: str) -> bool:
    current_time = datetime.now()
    start_time = current_time.replace(hour=2, minute=0, second=0, microsecond=0)
    end_time = current_time.replace(hour=4, minute=0, second=0, microsecond=0)
    
    cron = croniter(cron_expression, start_time)
    while True:
        next_time = cron.get_next(datetime)
        if next_time > end_time:
            break
        if next_time.hour >= 2 and next_time.hour <= 4:
            return True
    return False
import unittest


class TestIsCronBetween2And4AM(unittest.TestCase):

    def test_specific_hours(self):
        """should return true for specific hours 2, 3, and 4"""
        self.assertTrue(is_cron_between_2_and_4_am('0 2,3,4 * * *'))

    def test_range_includes_2_to_4_am(self):
        """should return false for range that includes 2 to 4 a.m."""
        self.assertFalse(is_cron_between_2_and_4_am('0 1-5 * * *'))

    def test_range_excludes_2_to_4_am(self):
        """should return false for range that excludes 2 to 4 a.m."""
        self.assertFalse(is_cron_between_2_and_4_am('0 0-1,5-23 * * *'))

    def test_wildcard_in_hour_field(self):
        """should return false for wildcard in hour field"""
        self.assertFalse(is_cron_between_2_and_4_am('0 * * * *'))

if __name__ == '__main__':
    unittest.main()