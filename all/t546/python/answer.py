import csv
import sys


def read_tsv_data_from_std_input():
    reader = csv.reader(sys.stdin, delimiter='\t')

    # Read all rows into a list
    data = [row for row in reader]

    # Find the maximum number of columns in the input data
    max_columns = max(len(row) for row in data) if data else 0

    # Pad all rows to ensure they have the same length
    padded_data = [row + [''] * (max_columns - len(row)) for row in data]

    return padded_data
