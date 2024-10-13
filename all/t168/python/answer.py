from datetime import datetime

def format_date(date_string: str) -> str:
    """
    Converts a date string into a relative time description.

    :param date_string: The date string to convert.
    :return: A user-friendly string representing the relative time difference from the current date.
    :raises ValueError: If the date string is invalid.
    """
    try:
        date = datetime.fromisoformat(date_string)  # Assuming the date string is in ISO format
    except ValueError:
        raise ValueError('Invalid Date')

    current_date = datetime.now()
    time_difference = current_date - date

    # Calculate time differences in seconds, minutes, hours, and days
    seconds_difference = int(time_difference.total_seconds())
    minutes_difference = seconds_difference // 60
    hours_difference = minutes_difference // 60
    days_difference = hours_difference // 24

    # Determine and return the appropriate time description
    if days_difference > 0:
        return f"{days_difference} day{'s' if days_difference != 1 else ''} ago"
    elif hours_difference > 0:
        return f"{hours_difference} hour{'s' if hours_difference != 1 else ''} ago"
    elif minutes_difference > 0:
        return f"{minutes_difference} minute{'s' if minutes_difference != 1 else ''} ago"
    else:
        return f"{seconds_difference} second{'s' if seconds_difference != 1 else ''} ago"