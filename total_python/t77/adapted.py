from datetime import datetime
import zoneinfo

def format_datetime_str(mtime: float, format: str = '%a %b %d %I:%M:%S %p %z %Y') -> str:
    """
    Convert a UNIX timestamp to a formatted datetime string using the system's local timezone.

    Args:
        mtime (float): UNIX timestamp.
        format (str): Format string for `strftime`.

    Returns:
        str: Formatted datetime string.
    """
    try:
        # Get the local system timezone
        local_tz = zoneinfo.ZoneInfo('localtime')
    except zoneinfo.ZoneInfoNotFoundError:
        # Fallback to UTC if the local timezone is not found
        local_tz = zoneinfo.ZoneInfo('UTC')

    try:
        # Convert the UNIX timestamp to a datetime object with timezone
        dt = datetime.fromtimestamp(mtime, tz=local_tz)
        # Return the formatted datetime string
        return dt.strftime(format)
    except Exception as e:
        # Handle any other unexpected errors
        raise ValueError(f"Error formatting the datetime: {e}")