import re


def sanitize_filename(filename: str) -> str:
    """
    Sanitize a string to make it comply with Windows filename rules.

    Args:
    filename (str): The original filename string to be sanitized.

    Returns:
    str: A sanitized string that is safe to use as a Windows filename.
    """
    # Remove illegal characters
    illegal_chars = r'[<>:"/\\|?*]'
    filename = re.sub(illegal_chars, '', filename)

    # Replace multiple spaces with a single space
    filename = re.sub(r'\s+', ' ', filename).strip()

    # Remove trailing period if any (Windows filenames cannot end with a period)
    if filename.endswith('.'):
        filename = filename.rstrip('.')

    return filename
