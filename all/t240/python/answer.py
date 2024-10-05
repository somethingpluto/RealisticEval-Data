from datetime import timedelta
import re


def gen_timeout_timedelta(time_string: str) -> timedelta:
    """
    Converts a time duration string into a timedelta object.
    The input string can include days (d), hours (h), minutes (m), seconds (s), and milliseconds (ms).
    eg. "1d 2h 3m 4s 500ms"
    Each unit should be specified by an integer followed by its corresponding unit letter.

    Args:
        time_string (str): A string representing the time duration.

    Returns:
        timedelta: A timedelta object representing the input duration.
    """
    # Define a dictionary to hold all our values
    time_values = {'d': 0, 'h': 0, 'm': 0, 's': 0, 'ms': 0}

    # Regular expression to find all parts of the time string
    parts = re.findall(r'(\d+)([dhms]{1,2})', time_string)

    # Process each found part
    for amount, unit in parts:
        if unit == 'd':
            time_values['d'] = int(amount)
        elif unit == 'h':
            time_values['h'] = int(amount)
        elif unit == 'm':
            time_values['m'] = int(amount)
        elif unit == 's':
            time_values['s'] = int(amount)
        elif unit == 'ms':
            time_values['ms'] = int(amount)

    # Create a timedelta object using the extracted values
    return timedelta(days=time_values['d'], hours=time_values['h'], minutes=time_values['m'],
                     seconds=time_values['s'], milliseconds=time_values['ms'])