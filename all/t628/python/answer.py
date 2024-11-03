def modify_line_in_file(file_path, line_number, new_value):
    """
    Modifies a specific line in the given file.

    :param file_path: the path of the file to be modified
    :param line_number: the line number to be modified (1-based index)
    :param new_value: the new value to update the line with
    :raises ValueError: if an invalid line number is specified
    """
    # Read the current lines of the file
    lines = []
    try:
        with open(file_path, 'r') as reader:
            lines = reader.readlines()
    except IOError as e:
        raise IOError(f"An error occurred while reading the file: {e}")

    # Check if the line number is valid
    if line_number < 1 or line_number > len(lines):
        raise ValueError(f"Invalid line number: {line_number}")

    # Update the specific line with the new value
    lines[line_number - 1] = new_value + '\n'  # Add newline character

    # Write the updated lines back to the file
    try:
        with open(file_path, 'w') as writer:
            writer.writelines(lines)
    except IOError as e:
        raise IOError(f"An error occurred while writing to the file: {e}")