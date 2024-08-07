# Generated with ChatGPT
def matrix_vector_multiplication(matrix, vector):
    if len(matrix[0]) != len(vector):
        raise ValueError("Matrix and vector dimensions are not compatible for multiplication")

    result = [0] * len(matrix)

    for i in range(len(matrix)):
        for j in range(len(vector)):
            result[i] += matrix[i][j] * vector[j]

    return result