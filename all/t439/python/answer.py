from typing import Any, Dict, List


def print_fixed_width_table(table: Dict[str, List[Any]]) -> None:
    """
    Prints a table formatted with fixed-width columns from a given dictionary.

    Parameters:
    table (dict[str, list[Any]]): A dictionary where the keys are column names
                                   and values are lists of column data.
    """
    # Extract keys (column names) and values (rows of data) from the dictionary
    keys = list(table.keys())
    values = list(table.values())

    # Transpose the values to get rows instead of columns
    transposed_values = list(zip(*values))

    # Calculate the maximum width of each column
    widths = [max(len(str(item)) for item in column) for column in transposed_values]

    # Include header lengths in widths
    widths = [max(width, len(key)) for width, key in zip(widths, keys)]

    # Format and print the header
    header = " ".join(f"{key:<{width}}" for key, width in zip(keys, widths))
    print(header)

    # Format and print each row
    for row in transposed_values:
        formatted_row = " ".join(f"{str(item):<{width}}" for item, width in zip(row, widths))
        print(formatted_row)