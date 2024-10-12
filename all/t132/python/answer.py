import os

def read_file(file_path):
    """
    Reads the content of a file synchronously and returns it as a string.

    :param file_path: The path to the file to be read.
    :return: The content of the file as a UTF-8 encoded string.
    :raises IOError: Raises an IOError if the file cannot be read.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as error:
        raise IOError(f"Failed to read file at {file_path}: {error}")

def write_file(file_path, data):
    """
    Writes data to a file synchronously.

    :param file_path: The path to the file where data will be written.
    :param data: The data to be written to the file.
    :raises IOError: Raises an IOError if the file cannot be written.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)
    except Exception as error:
        raise IOError(f"Failed to write file at {file_path}: {error}")
