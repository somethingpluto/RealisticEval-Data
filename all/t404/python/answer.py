from typing import List


def multiply_matrices(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    """Multiplies two matrices A and B and returns the result."""
    return [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]


def power(matrix: List[List[int]], n: int) -> List[List[int]]:
    """
    Computes the n-th power of a matrix using the fast exponentiation method.

    Args:
        matrix (List[List[int]]): A square matrix to be exponentiated.
        n (int): The exponent to raise the matrix to. Must be a non-negative integer.

    Returns:
        List[List[int]]: The matrix raised to the power of n.

    Raises:
        ValueError: If n is negative.
        TypeError: If matrix is not a list of lists or n is not an integer.
    """
    if n < 0:
        raise ValueError("The exponent n must be a non-negative integer.")
    if not isinstance(n, int):
        raise TypeError("The exponent n must be an integer.")

    # Identity matrix of the same size as the input matrix
    result = [[1 if i == j else 0 for j in range(len(matrix))] for i in range(len(matrix))]

    base = matrix.copy()

    while n > 0:
        if n % 2 == 1:
            result = multiply_matrices(result, base)
        base = multiply_matrices(base, base)
        n //= 2

    return result
