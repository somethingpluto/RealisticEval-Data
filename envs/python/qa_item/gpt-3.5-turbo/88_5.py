import re

def is_cron_between_2_and_4_am(cron_expression: str) -> bool:
    def parse_hours(hours_str):
        hours = set()
        if hours_str == "*":
            return set(range(24))
        for part in hours_str.split(","):
            if "-" in part:
                start, end = map(int, part.split("-"))
                hours.update(range(start, end + 1))
            else:
                hours.add(int(part))
        return hours

    hours = set()
    cron_parts = cron_expression.split()
    if len(cron_parts) >= 2:
        hours = parse_hours(cron_parts[1])

    return any(hour in hours for hour in range(2, 5))
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