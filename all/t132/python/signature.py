def read_file(file_path: str) -> str:
    """Reads the content of a file synchronously and returns it as a string.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str: The content of the file as a UTF-8 encoded string.

    Raises:
        OSError: Throws an error if the file cannot be read.
    """



def write_file(file_path: str, data: str) -> None:
    """Writes question to a file synchronously.

    Args:
        file_path (str): The path to the file where the question will be written.
        data (str): The question to be written to the file.

    Raises:
        OSError: Throws an error if the file cannot be written.
    """
