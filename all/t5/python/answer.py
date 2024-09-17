from typing import List


def matrix_multiply(matrixA: List[List[int]], matrixB: List[List[int]]) -> List[List[int]]:
    """
    Implementing matrix multiplication
    Args:
        matrixA (): matrix A
        matrixB (): matrix B

    Returns: matrixA matrixB multiplication model_answer_result

    """
    if not matrixA or not matrixB or not matrixA[0] or not matrixB[0]:
        return []
    # Ensure matrix dimensions are compatible for multiplication
    if len(matrixA[0]) != len(matrixB):
        raise ValueError(
            "The number of columns in the first matrix must be equal to the number of rows in the second matrix.")

    # Initialize the model_answer_result matrix with zeros
    result = [[0 for _ in range(len(matrixB[0]))] for _ in range(len(matrixA))]

    # Perform matrix multiplication
    for i in range(len(matrixA)):
        for j in range(len(matrixB[0])):
            for k in range(len(matrixB)):
                result[i][j] += matrixA[i][k] * matrixB[k][j]

    return result
