import re

def compress_filename(filename: str, max_length: int) -> str:
    """
    Compresses the filename before the extension, truncating it to a maximum length,
    and replacing the excess with '***' if it exceeds the specified maximum length.

    Args:
        filename (str): The full filename with or without an extension.
        max_length (int): The maximum allowed length of the filename before the extension.

    Returns:
        str: The compressed filename with its extension preserved.
    """
    # Extract the file extension using a regular expression
    extension_match = re.search(r'\.[^\.]+$', filename)
    extension = extension_match.group(0) if extension_match else ''

    # Remove the extension from the filename for manipulation
    basename = filename[:-len(extension)] if extension else filename

    # Compress the basename if it's longer than max_length
    compressed_basename = basename[:max_length - 3] + '***' if len(basename) > max_length else basename

    # Reattach the extension and return
    return compressed_basename + extension