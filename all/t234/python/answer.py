import csv


def append_or_skip_row(file_handler, reader, row_candidate):
    """
    Appends a new row to a CSV file if there isn't a row with matching values in the first three columns.

    :param file_handler: File handler of the CSV file opened in read-plus mode ('r+').
    :param reader: CSV reader object for reading existing rows.
    :param row_candidate: List containing the new row to be appended.
    """
    # Read existing rows into a list
    existing_rows = list(reader)

    # Check if a matching row exists in the first three columns
    for row in existing_rows:
        if row[:3] == row_candidate[:3]:  # Compare only the first three columns
            print("Row already exists. Skipping append.")
            return  # Skip appending if a match is found

    # Append the new row if no matching row is found
    file_handler.write('\n')  # Ensure there's a newline before appending
    writer = csv.writer(file_handler)
    writer.writerow(row_candidate)