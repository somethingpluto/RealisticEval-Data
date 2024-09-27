def append_or_skip_row(file_handler, reader, row_candidate):
    """
    Appends a new row to a CSV file if there isn't a row with matching values in the first three columns.

    Args:
        file_handler: File handler of the CSV file opened in read-plus mode ('r+').
        reader: CSV reader object for reading existing rows.
        row_candidate: List containing the new row to be appended.

    Returns:

    """
