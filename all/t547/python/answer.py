def calculate_column_widths(data):
    # Initialize a list to hold the maximum widths for each column.
    # This assumes that all rows in data have the same number of columns.
    widths = [0] * len(data[0])

    # Iterate over each row in the data.
    for row in data:
        # Iterate over each column in the row.
        for idx, col in enumerate(row):
            # Update the width at index `idx` with the maximum of the current width
            # and the length of the string in the current column.
            widths[idx] = max(widths[idx], len(col))

    # Return the list of maximum widths for each column.
    return widths