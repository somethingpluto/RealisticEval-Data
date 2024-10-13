import datetime

def get_current_date() -> str:
    """Get the current date in YYYY-MM-DD format."""
    # Get the current time
    now = datetime.datetime.now()
    # Format the date as a string
    formatted_date = now.strftime("%Y-%m-%d")
    return formatted_date
