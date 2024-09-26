import re


def sanitize_filename(filename: str) -> str:
    """
    Remove illegal characters from Windows file path string.

    Args:
        filename (str): The original filename string to be sanitized.

    Returns:
        str: A sanitized string that is safe to use as a Windows filename.
    """
    # Define the illegal characters for Windows filenames
    illegal_chars_pattern = r'[<>:"/\\|?*\x00-\x1F]'

    # Replace illegal characters with an underscore
    sanitized = re.sub(illegal_chars_pattern, '_', filename)

    # Optionally, you can also limit the length of the filename
    # Windows has a maximum path length of 260 characters
    max_length = 255
    if len(sanitized) > max_length:
        sanitized = sanitized[:max_length]

    return sanitized

