from typing import List


def multiply_matrices(mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
    """
    Multiply two matrices.

    Args:
        mat1 (List[List[int]]): The first matrix.
        mat2 (List[List[int]]): The second matrix.

    Returns:
        List[List[int]]: The result of multiplying mat1 by mat2.
    """
    # Number of rows in mat1
    rows_mat1 = len(mat1)
    # Number of columns in mat2
    cols_mat2 = len(mat2[0])
    # Number of columns in mat1 / rows in mat2
    common_dim = len(mat2)

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_mat2)] for _ in range(rows_mat1)]

    for i in range(rows_mat1):
        for j in range(cols_mat2):
            result[i][j] = sum(mat1[i][k] * mat2[k][j] for k in range(common_dim))

    return result
