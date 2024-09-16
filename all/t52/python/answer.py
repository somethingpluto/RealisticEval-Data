import os


def rename_file_path(path):
    """
    Renames a Windows file path by replacing colons in the filename with underscores.

    Parameters:
        path (str): The original file path.

    Returns:
        str: The modified file path with colons in the filename replaced by underscores.
    """
    # Split the path into directory and filename
    directory, filename = os.path.split(path)

    # Replace colons in the filename with underscores
    sanitized_filename = filename.replace(':', '_')

    # Reconstruct the full path with the sanitized filename
    new_path = os.path.join(directory, sanitized_filename)

    return new_path