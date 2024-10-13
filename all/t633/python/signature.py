import csv
from typing import List


def read_csv(file_path: str) -> List[List[str]]:
    """
    Reads a CSV file and parses each line into a list of strings.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        List[List[str]]: A list of string lists, where each list represents a line from the CSV.
    """
