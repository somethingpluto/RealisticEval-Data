from datetime import datetime

def is_same_day(timestamp1: int, timestamp2: int) -> bool:
    """
    Checks if two timestamps correspond to the same day.

    :param timestamp1: The first timestamp to compare.
    :param timestamp2: The second timestamp to compare.
    :returns: True if both timestamps are on the same day, false otherwise.
    """
    # Convert timestamps to datetime objects
    date1 = datetime.fromtimestamp(timestamp1)
    date2 = datetime.fromtimestamp(timestamp2)

    # Compare the year, month, and day of both datetime objects
    return (date1.year == date2.year and
            date1.month == date2.month and
            date1.day == date2.day)
