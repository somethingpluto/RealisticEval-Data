def multiply_matrices(mat1, mat2):
    # Initialize the result matrix with zeros of the appropriate size.
    result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]

    # Perform matrix multiplication
    for i in range(len(mat1)):  # Loop over rows of mat1
        for j in range(len(mat2[0])):  # Loop over columns of mat2
            # Calculate the value for each cell in the result matrix
            result[i][j] = sum(mat1[i][k] * mat2[k][j] for k in range(len(mat2)))

    return result
