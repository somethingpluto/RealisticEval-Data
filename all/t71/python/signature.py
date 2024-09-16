import numpy as np


def read_columns(file_name: str) -> np.array:
    """
    Reads numerical columns from a file starting from the line after the last line containing '/'.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        numpy.ndarray: A 2D numpy array containing the numerical question.

    Raises:
        ValueError: If the file does not contain any '/' character.
    """
