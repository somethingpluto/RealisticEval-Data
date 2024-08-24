import re
from typing import Optional


def convert_hms_to_milliseconds(time_str: str) -> Optional[int]:
    """
    Convert a time duration string in the format 'XhYminZs' to milliseconds.

    This function takes a string representing a time duration, where hours, minutes, and seconds
    are optionally provided, and converts this duration into the equivalent number of milliseconds.

    Args:
        time_str (str): A string representing the time duration, e.g., '1h20min30s'.

    Returns:
        Optional[int]: The equivalent duration in milliseconds, or None if the input is invalid.
    """
    # Regex to match hours, minutes, and seconds
    regex = r'^(?:(\d+)h)?(?:(\d+)min)?(?:(\d+)s)?$'
    match = re.search(regex, time_str)

    if not match:
        print(f'remindme.py: Cannot convert time string "{time_str}" to milliseconds!')
        return None

    # Extract hours, minutes, and seconds from the regex groups, defaulting to 0 if not present
    hours = int(match.group(1)) if match.group(1) else 0
    minutes = int(match.group(2)) if match.group(2) else 0
    seconds = int(match.group(3)) if match.group(3) else 0

    # Convert the total time to milliseconds
    milliseconds = ((hours * 60 + minutes) * 60 + seconds) * 1000

    return milliseconds
