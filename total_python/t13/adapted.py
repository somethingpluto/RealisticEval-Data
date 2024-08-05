def parse_markdown_table(markdown_table: str) -> list[tuple[str, ...]]:
    """
    Parses a Markdown formatted table string and returns a list of tuples,
    each representing a row in the table, including the header row.
    """
    lines = markdown_table.strip().split("\n")
    column_names = [name.strip() for name in lines[0].split("|")[1:-1]]
    num_columns = len(column_names)

    # Initialize a list to hold the data for each column
    column_data = [[] for _ in range(num_columns)]

    # Process the data rows, skipping the header separator row (lines[1])
    for line in lines[2:]:
        cells = [cell.strip() for cell in line.split("|")[1:-1]]
        if len(cells) != num_columns:
            raise ValueError(f"Row contains {len(cells)} cells, expected {num_columns}")

        for index, cell in enumerate(cells):
            column_data[index].append(cell)

    # Combine the column names with the data from each column
    return [tuple(column_names)] + list(zip(*column_data))
