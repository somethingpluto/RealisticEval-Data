import re


def convert_time_hms_string_to_ms(s):
    """
    Converts a time duration string in hours, minutes, and seconds format to milliseconds.

    Args:
    s (str): The time duration string (e.g., '2h15m30s').

    Returns:
    int: The time duration in milliseconds.

    Raises:
    ValueError: If the input string is not formatted correctly or if the time exceeds one day.
    """
    # Define the regex to parse the input string.
    if s == "":
        raise ValueError("str is empty")
    regex = r'(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?$'
    match = re.fullmatch(regex, s)

    # Check if the input is parsed correctly.
    if not match:
        raise ValueError(f"Cannot convert hms string '{s}' to ms - format is incorrect.")

    # Extract hours, minutes, and seconds from the match, defaulting to 0 if not found.
    hours = int(match.group(1)) if match.group(1) else 0
    minutes = int(match.group(2)) if match.group(2) else 0
    seconds = int(match.group(3)) if match.group(3) else 0

    # Convert the time to milliseconds.
    ms = ((hours * 60 + minutes) * 60 + seconds) * 1000

    # Check if the calculated milliseconds exceed the number of milliseconds in one day.
    if ms > 86400000:
        raise ValueError("Total time cannot exceed one day (86400000 ms).")

    return ms
