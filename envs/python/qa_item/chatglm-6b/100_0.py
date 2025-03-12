
def convert_time(duration: str) -> str:
    """
    Converts an ISO 8601 duration string into a more readable format.

    Args:
        duration (str): The ISO 8601 duration string (e.g., "PT1H23M45.678S").

    Returns:
        str: A human-readable duration string (e.g., "1h23m45s678ms").
    """
    # Split the duration string into an array of duration elements
    duration_elements = duration.split(" ")

    # Initialize a dictionary to store the duration elements
    duration_dict = {}

    # Loop through the duration elements and convert them to a human-readable format
    for element in duration_elements:
        # Split the element into a time and a duration part
        time, duration = element.split("T")

        # Add the time part to the dictionary
        duration_dict[time] = duration

        # Update the time part with the current timestamp
        time = int(time)

    # Convert the dictionary to a string
    human_readable_duration = ""
    for key, value in duration_dict.items():
        human_readable_duration += f"{key}:{value}"

    return human_readable_duration

import unittest


class TestConvertTimeFunction(unittest.TestCase):

    def test_full_iso_duration(self):
        """Test converting full ISO 8601 duration with hours, minutes, seconds, and milliseconds."""
        self.assertEqual(convert_time('PT1H23M45.678S'), '1h23m45s678ms')

    def test_duration_with_seconds_and_milliseconds(self):
        """Test converting duration with only seconds and milliseconds."""
        self.assertEqual(convert_time('PT45.5S'), '45s500ms')

    def test_duration_with_hours_and_minutes_no_seconds(self):
        """Test converting duration with hours and minutes, but no seconds."""
        self.assertEqual(convert_time('PT2H5M'), '2h5m')

    def test_duration_with_only_seconds_no_milliseconds(self):
        """Test converting duration with only seconds, no milliseconds."""
        self.assertEqual(convert_time('PT20S'), '20s')

if __name__ == '__main__':
    unittest.main()