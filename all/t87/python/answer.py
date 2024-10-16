from datetime import datetime


def convert_unix_timestamp_to_readable_date(unix_timestamp: int) -> str:
    # Convert Unix timestamp to a datetime object
    date = datetime.fromtimestamp(unix_timestamp)

    # List of month names
    month_names = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ]

    # Get month, day, hours, and minutes
    month = month_names[date.month - 1]  # Adjust for 0-indexed list
    day = date.day
    hours = date.hour
    minutes = str(date.minute).zfill(2)  # Pad minutes with zero if necessary

    # Return formatted date string
    return f"{month} {day}, {hours}:{minutes}"