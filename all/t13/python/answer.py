from typing import List


def parse_markdown_table(md_table: str) -> List[tuple]:
    """
    Parses a Markdown formatted table into a list of tuples, each tuple representing a row.

    Args:
        md_table (str): A string representing a Markdown table.

    Returns:
        list of tuples: A list where each tuple represents a row in the table.
    """
    # Split the input string into lines and strip whitespace
    lines = md_table.strip().split('\n')

    # Filter out the separator line for the header (which usually contains "---")
    lines = [line for line in lines if not '---' in line.strip()]

    # Initialize the list to store each row as a tuple
    table_data = []

    # Process each line
    for line in lines:
        # Strip leading and trailing spaces and pipes, then split by "|"
        row = line.strip().strip('|').split('|')
        # Process each cell, strip spaces, handle empty cells, and create a tuple
        tuple_row = tuple(cell.strip() if cell.strip() != '' else '' for cell in row)
        # Add the tuple to the list
        table_data.append(tuple_row)

    return table_data