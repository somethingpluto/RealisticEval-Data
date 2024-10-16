from typing import List


def get_common_columns_from_csvs(directory: str) -> List:
    """
    find the common columns of all csv files in a directory and return these column names as a list
    Args:
        directory (str): directory path

    Returns:
        same column list
    """
