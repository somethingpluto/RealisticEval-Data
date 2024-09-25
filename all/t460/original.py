# Generated with ChatGPT
def matrix_vector_multiplication(matrix, vector):
    if len(matrix[0]) != len(vector):
        raise ValueError("Matrix and vector dimensions are not compatible for multiplication")

    result = [0] * len(matrix)

    for i in range(len(matrix)):
        for j in range(len(vector)):
            result[i] += matrix[i][j] * vector[j]

    return result

# Example usage:
matrix = [[1, 2, 3], [4, 5, 6]]
vector = [7, 8, 9]
result = matrix_vector_multiplication(matrix, vector)
print(result)