def create_matrix(rows, columns, initial_value):
    # Initialize the matrix as an empty list
    matrix = []
    # Loop through each row
    for i in range(rows):
        # Create a new row list filled with the initial value
        row = [initial_value] * columns
        # Add the filled row to the matrix
        matrix.append(row)
    return matrix