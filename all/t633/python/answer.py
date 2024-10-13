import csv
from typing import List


def read_csv(file_path: str) -> List[List[str]]:
    """
    Reads a CSV file and parses each line into a list of strings.

    :param file_path: The path to the CSV file.
    :return: A list of string lists, where each list represents a line from the CSV.
    """
    csv_data = []
    # Read the CSV file
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        # Parse each line into a list of strings
        for row in reader:
            csv_data.append(row)
    return csv_data