import re


def extract_date_from_filename(file_name: str):
    """
    Extracts the date in the format YYYY-MM-DD from the given file name.

    Args:
        file_name (str): The name of the file which may contain a date.

    Returns:
        str or None: The extracted date string in YYYY-MM-DD format if found, else None.
    """
