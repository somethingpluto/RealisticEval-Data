from typing import List


def matrix_vector_multiplication(matrix: List[List[float]], vector: List[float]) -> List[float]:
    """
    Multiplies a matrix by a vector and returns the resulting vector.

    Args:
        matrix (List[List[float]]): A 2D list representing the matrix.
        vector (List[float]): A 1D list representing the vector.

    Returns:
        List[float]: The resulting vector after multiplication.

    Raises:
        ValueError: If the dimensions of the matrix and vector are not compatible for multiplication.
    """
