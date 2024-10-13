def format_date(date_string: str) -> str:
    """
    Converts a date string into a relative time description.
    For example, now time 2024-08-25T12:00:00
         input: 2024-08-24T12:00:00 output: 1 day ago
         input: 2024-08-25T07:00:00 output: 5 hours ago

    Args:
        date_string (str): The date string to convert.

    Returns:
        str: A user-friendly string representing the relative time difference from the current date.
    """