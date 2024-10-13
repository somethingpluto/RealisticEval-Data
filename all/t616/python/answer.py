def byte_count_to_display_size(size_in_bytes: int) -> str:
    """Converts a size in bytes to a human-readable string representation.

    Args:
        size_in_bytes (int): The size in bytes to convert.

    Returns:
        str: A string representation of the size in an appropriate unit (bytes, KB, MB, GB, TB).
    """
    # Check the size and format accordingly
    ONE_KB = 1024
    ONE_MB = ONE_KB * 1024
    ONE_GB = ONE_MB * 1024
    ONE_TB = ONE_GB * 1024
    if size_in_bytes < ONE_KB:
        return f"{size_in_bytes:.2f} bytes"  # Return size in bytes
    elif size_in_bytes < ONE_MB:
        return f"{size_in_bytes / ONE_KB:.2f} KB"  # Return size in KB
    elif size_in_bytes < ONE_GB:
        return f"{size_in_bytes / ONE_MB:.2f} MB"  # Return size in MB
    elif size_in_bytes < ONE_TB:
        return f"{size_in_bytes / ONE_GB:.2f} GB"  # Return size in GB
    else:
        return f"{size_in_bytes / ONE_TB:.2f} TB"  # Return size in TB