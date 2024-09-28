def dict_list_to_markdown_table(data):
    """
    Convert a list of dictionaries to a Markdown formatted table.

    :param data: List of dictionaries to be converted.
    :return: A string representing the Markdown formatted table.
    """
    if not data:
        return "No data available."

    # Get the headers from the keys of the first dictionary
    headers = data[0].keys()

    # Create the header row
    header_row = "| " + " | ".join(headers) + " |"

    # Create the separator row
    separator_row = "| " + " | ".join(['---'] * len(headers)) + " |"

    # Create the data rows
    data_rows = []
    for entry in data:
        row = "| " + " | ".join(str(entry[key]) for key in headers) + " |"
        data_rows.append(row)

    # Combine all rows into a single string
    table = "\n".join([header_row, separator_row] + data_rows)

    return table