def get_file_size(size_in_bytes, unit=None):
    if unit is None:
        if size_in_bytes < 1024:
            return f"{size_in_bytes} B", size_in_bytes / (1024**2)
        elif size_in_bytes < 1024**2:
            return f"{size_in_bytes / 1024:.2f} KB", size_in_bytes / (1024**2)
        elif size_in_bytes < 1024**3:
            return f"{size_in_bytes / (1024**2):.2f} MB", size_in_bytes / (1024**2)
        else:
            return f"{size_in_bytes / (1024**3):.2f} GB", size_in_bytes / (1024**2)
    else: 
        unit = unit.upper()
        if unit == 'B':
            return f"{size_in_bytes} B", size_in_bytes / (1024**2)
        elif unit == 'KB':
            return f"{size_in_bytes / 1024:.2f} KB", size_in_bytes / (1024**2)
        elif unit == 'MB':
            return f"{size_in_bytes / (1024**2):.2f} MB", size_in_bytes / (1024**2)
        elif unit == 'GB':
            return f"{size_in_bytes / (1024**3):.2f} GB", size_in_bytes / (1024**2)