from datetime import datetime

def format_date_string(date_str:str):
    """
    Converts a date string from the format '%a, %d %b %Y %H:%M:%S %z (%Z)'
    to the format '%Y-%m-%d_%H:%M:%S'.

    Args:
        date_str (str): The input date string.

    Returns:
        str: The formatted date string in the format '%Y-%m-%d_%H:%M:%S'.
        None: If the input date string is invalid.
    """