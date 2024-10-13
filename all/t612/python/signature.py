def find_and_replace_in_file(file_path:str, search_string:str, replace_string:str):
    """
    Finds and replaces text in a specified file.

    Args:
        file_path (str): The path to the file.
        search_string (str): The string to search for.
        replace_string (str): The string to replace with.

    Raises:
        IOError: If an I/O error occurs reading from the file or writing to the file.
    """