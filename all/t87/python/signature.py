from datetime import datetime


def convert_unix_timestamp_to_readable_date(unix_timestamp: int) -> str:
    """
    Convert the UNIX timestamp to the string format 'MMM D, H:MM'.

    Example:
        Input: 1672531200
        Output: 'Jan 1, 8:00'

        Input: 1696516800
        Output: 'Oct 5, 22:40'

    Args:
        unix_timestamp (int): The UNIX timestamp to convert.

    Returns:
        str: A formatted date string in the form 'MMM D, H:MM'.
    """