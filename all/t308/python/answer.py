from datetime import datetime

def get_current_date():
    # Get the current date and format it as YYYY-MM-DD
    current_date = datetime.now()  # Get the current date and time
    return current_date.strftime('%Y-%m-%d')  # Format the date as YYYY-MM-DD
