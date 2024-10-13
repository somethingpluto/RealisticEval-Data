import re


def convert_time_hms_string_to_ms(time_str: str) -> int:
    """
    Converts a time string in the format "XhYmZs" (hours, minutes, seconds) into milliseconds.

    Args:
        time_str (str): The input string representing the time duration.

    Returns:
        int: The time in milliseconds.

    Raises:
        ValueError: If the input string does not match the expected format.
    """
    # Regular expression to parse the string for hours, minutes, and seconds
    regex = r'(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?'
    match = re.match(regex, time_str)

    # Raise an error if the string does not match the expected format
    if not match:
        raise ValueError(f'Cannot convert hms string "{time_str}" to ms!')

    # Parse hours, minutes, and seconds, defaulting to 0 if any group is missing
    hours = int(match.group(1) or '0')
    minutes = int(match.group(2) or '0')
    seconds = int(match.group(3) or '0')

    # Calculate the total milliseconds
    total_milliseconds = ((hours * 60 + minutes) * 60 + seconds) * 1000
    return total_milliseconds