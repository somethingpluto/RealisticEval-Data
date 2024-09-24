from typing import Optional

def format_timestamp_to_string(timestamp: float, date_format: Optional[str] = '%a %b %d %I:%M:%S %p %z %Y') -> str:
    """
    Formats the given timestamp as a string according to the specified format, using the system's local time zone.

    Args:
        timestamp (float): The time value representing the seconds since the epoch.
        date_format (Optional[str]): The format string to use for formatting the timestamp.
                                     Defaults to '%a %b %d %I:%M:%S %p %z %Y'.

    Returns:
        str: The formatted date and time string.
    """