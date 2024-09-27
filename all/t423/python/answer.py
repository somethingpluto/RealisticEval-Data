def write_unique_line_to_file(filename: str, line_content: str):
    """
    Writes a line to a text file only if the line with the same content does not already exist.

    Args:
        filename (str): The name of the file to write to.
        line_content (str): The content of the line to write.

    Returns:
        None
    """
    # Check if the line_content already exists in the file
    with open(filename, 'r') as file:
        if line_content in file.read():
            print(f"Line '{line_content}' already exists in '{filename}'. Not writing again.")
            return

    # If line_content is not found, append it to the file
    with open(filename, 'a') as file:
        file.write(line_content + '\n')
        print(f"Line '{line_content}' successfully written to '{filename}'.")