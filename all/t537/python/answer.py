from datetime import datetime

def get_time() -> str:
    """
    Gets the current time formatted as 'hh:mm AM/PM'.

    Returns:
        str: The formatted time string.
    """
    current_date = datetime.now()  # Get the current date and time
    formatted_time = current_date.strftime('%I:%M %p')  # Format time as 'hh:mm AM/PM'
    return formatted_time