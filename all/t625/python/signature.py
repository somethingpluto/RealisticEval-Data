from typing import List, Union


def read_data_from_file(path: str) -> List[Union[int, float, str]]:
    """
    Reads data from a specified file and determines the type of each line.
    This function processes each line of the specified file and attempts to convert it
    into either an integer, a floating-point number, or a string.

    Args:
        path (str): The path to the file to be read. The file should exist and be accessible for reading.

    Returns:
        list: A list containing the converted values of each line in the file. Each element
              can be an int, float, or str, depending on the content of the line.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If the program lacks permissions to read the file.
        IOError: If an I/O error occurs while reading the file.
    """
