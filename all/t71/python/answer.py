import numpy as np


def read_columns(file_name):
    """
    Reads numerical columns from a file starting from the line after the last line containing '/'.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        numpy.ndarray: A 2D numpy array containing the numerical question.

    Raises:
        ValueError: If the file does not contain any '/' character.
    """
    # Initialize a variable to track the last slash line index
    last_slash_index = None

    with open(file_name) as f:
        lines = f.readlines()

    # Find the index of the last line that contains the "/" character
    for i, line in enumerate(lines):
        if "/" in line:
            last_slash_index = i

    # If no "/" character was found, raise an error
    if last_slash_index is None:
        raise ValueError("File does not contain '/' character")

    # Read the remaining lines in the file, starting from the line after the last "/"
    data_lines = lines[last_slash_index + 1:]

    # Remove any empty lines or lines that start with a comment character
    data_lines = [line.strip() for line in data_lines if line.strip() and not line.strip().startswith('!')]

    # If no valid lines remain, return an empty array
    if not data_lines:
        return np.array([])

    # Get the row and column count by counting the number of columns in the first line
    col_count = len(data_lines[0].split())

    # Create an empty numpy array of the required size
    arr = np.zeros((len(data_lines), col_count))

    # Loop through the lines in the file
    for i, line in enumerate(data_lines):
        # Split the line into numbers and convert them to floats
        nums = [float(x) for x in line.split()]
        # Store the numbers in the array
        arr[i, :] = nums

    # Return the array
    return arr
