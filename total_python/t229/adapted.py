def get_file_size(size_in_bytes, unit=None):
    """
    Converts a file size in bytes to a specified unit, or to an appropriately scaled unit if none is specified.

    Parameters:
    size_in_bytes (int): File size in bytes.
    unit (str, optional): The unit to convert the size to ('B', 'KB', 'MB', 'GB').

    Returns:
    tuple: A tuple containing the formatted size string and the size converted to the specified or chosen unit as float.
    """
    units = {
        'B': 1,
        'KB': 1024,
        'MB': 1024 ** 2,
        'GB': 1024 ** 3
    }

    if unit is None:
        # Automatically choose unit based on size
        if size_in_bytes < 1024:
            unit = 'B'
        elif size_in_bytes < 1024 ** 2:
            unit = 'KB'
        elif size_in_bytes < 1024 ** 3:
            unit = 'MB'
        else:
            unit = 'GB'
    else:
        unit = unit.upper()  # Normalize unit input to uppercase
        if unit not in units:
            raise ValueError("Invalid unit. Choose among 'B', 'KB', 'MB', 'GB'.")

    # Calculate the size in the chosen or specified unit
    size_in_unit = size_in_bytes / units[unit]

    # Format the size with two decimal places if not in bytes
    if unit == 'B':
        formatted_size = f"{size_in_bytes} B"
    else:
        formatted_size = f"{size_in_unit:.2f} {unit}"

    return formatted_size, size_in_unit
