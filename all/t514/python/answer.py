import re

def extract_date_from_filename(file_name):
    """
    Extracts the date in the format YYYY-MM-DD from the given file name.

    Args:
        file_name (str): The name of the file which may contain a date.

    Returns:
        str or None: The extracted date string in YYYY-MM-DD format if found, else None.
    """
    # Define the regex pattern for matching a date in the format YYYY-MM-DD
    date_pattern = r'\d{4}-\d{2}-\d{2}'
    
    # Search for the date pattern in the file name
    match = re.search(date_pattern, file_name)
    
    # If a match is found, return the matched date; otherwise, return None
    return match.group(0) if match else None