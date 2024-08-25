import re
from datetime import timedelta


def gen_timeout_timedelta(time_string):
    """
    Converts a time duration string into a timedelta object.

    The input string can include days (d), hours (h), minutes (m), seconds (s), and milliseconds (ms).
    Each unit should be specified by an integer followed by its corresponding unit letter.

    Args:
    time_string (str): A string representing the time duration.

    Returns:
    timedelta: A timedelta object representing the input duration.

    Raises:
    ValueError: If the input string is in an incorrect format.
    """
    # Regex pattern to extract days, hours, minutes, seconds, and milliseconds
    if time_string == "":
        raise ValueError("empty time str")
    pattern = r'(?:(\d+)\s*d)?\s*(?:(\d+)\s*h)?\s*(?:(\d+)\s*m)?\s*(?:(\d+)\s*s)?\s*(?:(\d+)\s*ms)?'
    matches = re.fullmatch(pattern, time_string.strip())

    if not matches:
        raise ValueError("Invalid time format")

    # Extracting time units from the match groups, defaulting to 0 if not present
    days, hours, minutes, seconds, milliseconds = (int(x) if x else 0 for x in matches.groups())

    # Creating a timedelta object from the extracted values
    return timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds, milliseconds=milliseconds)
