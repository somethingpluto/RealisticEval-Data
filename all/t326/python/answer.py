from datetime import datetime

def calculate_time_difference(given_date):
    """
    Calculates the time difference between a given date and the current date.

    :param given_date: The date to compare against the current date (string or datetime).
    :return: A dictionary containing days, hours, and minutes elapsed.
    {
        'days': days,
        'hours': remaining_hours,
        'minutes': remaining_minutes,
    }
    """
    # Convert given_date to a datetime object if it's a string
    if isinstance(given_date, str):
        date_to_compare = datetime.fromisoformat(given_date)  # Assuming ISO format
    else:
        date_to_compare = given_date

    current_date = datetime.now()

    # Calculate the difference in seconds
    difference_in_seconds = (current_date - date_to_compare).total_seconds()

    # If the given date is in the future
    if difference_in_seconds < 0:
        return {'days': 0, 'hours': 0, 'minutes': 0}

    # Calculate days, hours, and minutes
    minutes = int(difference_in_seconds // 60)
    hours = minutes // 60
    days = hours // 24

    # Calculate remaining hours and minutes
    remaining_hours = hours % 24
    remaining_minutes = minutes % 60

    return {
        'days': days,
        'hours': remaining_hours,
        'minutes': remaining_minutes,
    }
