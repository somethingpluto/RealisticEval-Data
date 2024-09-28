
def transposeMatrix(matrix):
    """
    Transpose a given matrix (2D array).

    Args:
    matrix (list): The input 2D array to be transposed.

    Returns:
    list: The transposed 2D array.
    """
    numRows = len(matrix)
    numCols = len(matrix[0])
    transposed = [[matrix[j][i] for j in range(numRows)] for i in range(numCols)]
    return transposed