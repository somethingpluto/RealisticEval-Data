from datetime import datetime


def get_date() -> str:
    """
    Gets the current date formatted as 'Month Day, Year'.

    Returns:
        str: The formatted date string.
    """
    # Create a new datetime object representing the current date and time
    current_date = datetime.now()

    # Format the date as 'Month Day, Year'
    formatted_date = current_date.strftime('%B %d, %Y')

    return formatted_date