from typing import Tuple


def get_file_size(size_in_bytes, unit=None) -> Tuple[int, float]:
    """
    Convert file size from bytes to a more readable format (e.g. KB, MB, GB)
    For example:
        input:

    Args:
        size_in_bytes (int): File size in bytes.
        unit (str, optional): The unit to convert the size to ('B', 'KB', 'MB', 'GB').

    Returns:
        tuple: A tuple containing the formatted size string and the size converted to the specified or chosen unit as float.
    """
