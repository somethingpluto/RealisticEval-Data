from typing import List


def parse_table(md_table: str) -> List[tuple[str, ...]]:
    """
    Created by ChatGPT 3.5 Turbo model
    """
    rows = md_table.strip().split("\n")
    # Get the column names from the first row
    col_names = [cell.strip() for cell in rows[0].split("|")[1:-1]]
    num_cols = len(col_names)
    # Initialize the table data as a list of empty lists
    table_data = [[] for i in range(num_cols)]
    # Parse the remaining rows
    for row in rows[2:]:
        # Split the row into cells
        cells = [cell.strip() for cell in row.split("|")[1:-1]]
        # Check that the row has the correct number of cells
        if len(cells) != num_cols:
            raise ValueError(f"Row has {len(cells)} cells, but expected {num_cols}")
        # Add each cell to the appropriate column in the table data
        for i, cell in enumerate(cells):
            table_data[i].append(cell)
    # Combine the column names with the table data and return the result
    return [col_names] + list(zip(*table_data))