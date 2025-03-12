
def is_cron_between_2_and_4_am(cron_expression: str) -> bool:
    """
    Parse a cron expression and determine whether it is between 2 a.m. and 4 a.m.

    Args:
        cron_expression (str): The cron expression to parse.

    Returns:
        bool: True if any hour in the cron expression is between 2 a.m. and 4 a.m., False otherwise.
    """
    # Parse the cron expression
    cron_hours = cron_expression.split(" ")[1].split(":")[0]
    hours = map(int, cron_hours.split(":"))
    cron_expression = "{} {}".format(hours, cron_hours.split(":")[0])

    # Check if the cron expression is valid
    if len(cron_hours)!= 6:
        return False
    if not cron_expression.startswith("0 ") and cron_expression[-5:]!= "0 ":
        return False

    # Get the hours of the day
    day_of_week = "Sun" if cron_expression[-5:] == "0 2" else "Mon"
    day = int(cron_expression[:-5].replace("0", ""))
    hour = int(cron_expression[-5:].replace("0", ""))

    # Check if the hours are between 2 and 4
    if day_of_week in ["Sun", "Mon"] and day < 7 and hour < 12:
        return True
    elif day_of_week in ["Sun", "Mon"] and day >= 7 and hour >= 12:
        return True
    else:
        return False

import unittest


class TestIsCronBetween2And4AM(unittest.TestCase):

    def test_specific_hours(self):
        """should return true for specific hours 2, 3, and 4"""
        self.assertTrue(is_cron_between_2_and_4_am('0 2,3,4 * * *'))

    def test_range_includes_2_to_4_am(self):
        """should return false for range that includes 2 to 4 a.m."""
        self.assertTrue(is_cron_between_2_and_4_am('0 2-4 * * *'))

    def test_range_excludes_2_to_4_am(self):
        """should return false for range that excludes 2 to 4 a.m."""
        self.assertFalse(is_cron_between_2_and_4_am('0 0-1,5-23 * * *'))

    def test_wildcard_in_hour_field(self):
        """should return false for wildcard in hour field"""
        self.assertFalse(is_cron_between_2_and_4_am('0 * * * *'))
if __name__ == '__main__':
    unittest.main()