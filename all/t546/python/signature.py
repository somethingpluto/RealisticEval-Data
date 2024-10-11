import csv
import sys


def read_tsv_from_stdin():
    """
    Reads tab-separated values (TSV) from standard input and returns a list of rows.

    Each row is represented as a list of strings. If rows have unequal lengths,
    they are padded with empty strings to ensure all rows have the same length.

    Returns:
        list: A list of lists, where each inner list represents a row of data.
    """
