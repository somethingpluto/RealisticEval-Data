from typing import List

def transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Transpose a given matrix (2D array).

    Args:
        matrix (List[List[int]]): The input 2D array to be transposed.

    Returns:
        List[List[int]]: The transposed 2D array.
    """
    # Check if the matrix is empty
    if not matrix or not matrix[0]:
        return []

    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    # Initialize the transposed matrix with the correct dimensions
    transposed = [[0] * num_rows for _ in range(num_cols)]

    for i in range(num_rows):
        for j in range(num_cols):
            transposed[j][i] = matrix[i][j]

    return transposed
