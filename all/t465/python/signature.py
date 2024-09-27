import numpy as np


def matrix_vector_multiplication(matrix: np.array, vector: np.array):
    """
    Multiplies a given matrix by a vector using NumPy's dot product.

    Parameters:
    matrix (numpy.ndarray): A 2D array (matrix) of shape (m, n) where m is the number of rows
                            and n is the number of columns.
    vector (numpy.ndarray): A 1D array (vector) of shape (n,) that represents a vector
                            compatible for multiplication with the given matrix.

    Returns:
    numpy.ndarray: A 1D array (resulting vector) of shape (m,) representing the product of
                   the matrix and the vector.
    """

    # Perform matrix-vector multiplication using the dot product function.
    result = np.dot(matrix, vector)

    # Return the resulting vector from the multiplication.
    return result
