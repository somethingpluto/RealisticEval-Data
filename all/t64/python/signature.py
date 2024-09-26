import csv
import os


def csv_to_sql_insert(csv_file_path: str) -> str:
    """
    Converts the contents of a csv file into an SQL insert statement with a table name with the suffix removed.

    Args:
        csv_file_path (str): csv file path

    Returns:
        str: parsed sql str
    """
