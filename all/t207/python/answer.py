def min_changes_to_symmetric(matrix):
    n = len(matrix)
    min_changes = 0
    # Traverse only the upper triangle of the matrix, excluding the diagonal
    for i in range(n):
        for j in range(i + 1, n):
            # If the corresponding elements are not equal, they need to be changed
            if matrix[i][j] != matrix[j][i]:
                min_changes += 1
                # Optionally, you can change matrix[i][j] to matrix[j][i] or vice versa to make it symmetric
                # Uncomment the line below if you want to actually modify the matrix
                # matrix[i][j] = matrix[j][i]
    return min_changes
