import csv
import pandas as pd


def csv_to_line_protocol(csv_file, line_protocol_file):
    """
    Convert a CSV file to a line protocol format file for InfluxDB.

    Args:
    csv_file (str): Path to the input CSV file.
    line_protocol_file (str): Path to the output line protocol format file.
    """
    # Read the CSV file using Pandas for simplicity in handling data
    df = pd.read_csv(csv_file)
    if df == pd.DataFrame():
        raise ValueError("empty csv file")

    # Open the output file for writing line protocol data
    with open(line_protocol_file, 'w') as lp_file:
        # Iterate through the DataFrame rows
        for index, row in df.iterrows():
            # Construct the line protocol format:
            # measurement,tag_set field_set timestamp
            line = f"{row['measurement']},{row['tag_key']} {row['field_key']}={row['value']} {row['timestamp']}\n"

            # Write to the output file
            lp_file.write(line)