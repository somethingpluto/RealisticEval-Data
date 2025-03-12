import re

def is_cron_between_2_and_4_am(cron_expression: str) -> bool:
    """
    Parse a cron expression and determine whether it is between 2 a.m. and 4 a.m.

    Args:
        cron_expression (str): The cron expression to parse.

    Returns:
        bool: True if any hour in the cron expression is between 2 a.m. and 4 a.m., False otherwise.
    """
    # Split the cron expression into its components
    cron_parts = cron_expression.split()
    
    # The hour part is the second element in the cron expression
    hour_part = cron_parts[1]
    
    # Define the range of hours we are interested in
    target_hours = {2, 3, 4}
    
    # Function to expand a cron range (e.g., "2-4" -> [2, 3, 4])
    def expand_range(range_str):
        if '-' in range_str:
            start, end = map(int, range_str.split('-'))
            return set(range(start, end + 1))
        return {int(range_str)}
    
    # Function to expand a cron list (e.g., "2,3,4" -> [2, 3, 4])
    def expand_list(list_str):
        return set(map(int, list_str.split(',')))
    
    # Function to expand a cron wildcard (e.g., "*" -> [0, 1, ..., 23])
    def expand_wildcard(wildcard_str):
        return set(range(24)) if wildcard_str == '*' else {int(wildcard_str)}
    
    # Expand the hour part based on its format
    if ',' in hour_part:
        hours = expand_list(hour_part)
    elif '-' in hour_part:
        hours = expand_range(hour_part)
    elif hour_part == '*':
        hours = expand_wildcard(hour_part)
    else:
        hours = {int(hour_part)}
    
    # Check if any of the expanded hours are within the target range
    return not target_hours.isdisjoint(hours)
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