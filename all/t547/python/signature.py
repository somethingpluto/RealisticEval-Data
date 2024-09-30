from typing import List


def calculate_column_widths(data: List[List[str]]) -> List[int]:
    """
    Calculate the maximum width of each column in a list of lists where each sub-list represents a row of table data.

    Args:
        data (List[List[str]]): A two-dimensional list containing rows of data, where each inner list contains string elements representing the values in each column.

    Returns:
        List[int]: A list containing the maximum width (in characters) of each column across all rows. The width of a column is defined by the longest string present in that column.
    """
