import re

def is_cron_between_2_and_4_am(cron_expression: str) -> bool:
    """
    Parse a cron expression and determine whether it is between 2 a.m. and 4 a.m.

    Args:
        cron_expression (str): The cron expression to parse.

    Returns:
        bool: True if any hour in the cron expression is between 2 a.m. and 4 a.m., False otherwise.
    """
    hour_range_regex = r'(\d{1,2})'
    hours = re.findall(hour_range_regex, cron_expression)
    
    for hour in hours:
        hour_int = int(hour)
        if hour_int >= 2 and hour_int <= 4:
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