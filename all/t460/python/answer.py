from typing import List

def matrix_vector_multiplication(matrix: List[List[float]], vector: List[float]) -> List[float]:
    # Ensure matrix dimensions are compatible with vector length
    if len(matrix[0]) != len(vector):
        raise ValueError("Matrix and vector dimensions are not compatible for multiplication")

    # Initialize the result list with zeros
    result = [0.0] * len(matrix)

    # Perform the matrix-vector multiplication
    for i in range(len(matrix)):
        for j in range(len(vector)):
            result[i] += matrix[i][j] * vector[j]

    return result