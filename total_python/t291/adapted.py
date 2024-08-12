def prepend_to_each_line(file_path, prefix):
    """
    Appends the specified string to the beginning of each line of the file.

    Args:
    file_path (str): Path to the file whose lines will be modified.
    prefix (str): String to append to the beginning of each line.
    """
    import os
    temp_file_path = file_path + ".tmp"

    with open(file_path, 'r') as file, open(temp_file_path, 'w') as temp_file:
        for line in file:
            temp_file.write(prefix + line)

    # Replace the original file with the modified file
    os.replace(temp_file_path, file_path)
