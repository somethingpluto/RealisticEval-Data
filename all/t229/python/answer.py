def convert_file_size(size_bytes):
    # Define the size units
    units = ['B', 'KB', 'MB', 'GB', 'TB']

    # Handle the case when size is 0 bytes
    if size_bytes == 0:
        return "0B"

    # Calculate the appropriate unit
    index = 0
    while size_bytes >= 1024 and index < len(units) - 1:
        size_bytes /= 1024
        index += 1

    # Return the formatted size with the appropriate unit
    return f"{int(size_bytes)}{units[index]}"
