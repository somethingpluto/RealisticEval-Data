from datetime import datetime

def format_date_string(date_str):
    """
    Converts a date string from the format '%a, %d %b %Y %H:%M:%S %z (%Z)'
    to the format '%Y-%m-%d_%H:%M:%S'.

    Args:
        date_str (str): The input date string.

    Returns:
        str: The formatted date string in the format '%Y-%m-%d_%H:%M:%S'.
        None: If the input date string is invalid.
    """
    try:
        # Convert to a datetime object using the specified format
        date_object = datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S %z (%Z)')

        # Convert to the desired output format
        formatted_date = date_object.strftime('%Y-%m-%d_%H:%M:%S')
        
        return formatted_date
    except ValueError as e:
        print(f"Error parsing date: {e}")
        return None
