import csv
from datetime import datetime


def excel_timestamp_to_datetime(excel_timestamp):
    """
    Convert Excel timestamp to datetime object.
    """
    return datetime.fromtimestamp((excel_timestamp - 25569) * 86400.0)


def convert_csv_values(row):
    """
    Convert CSV row values from strings to appropriate data types.
    """
    for key, value in row.items():
        try:
            if key == 'distance':
                row[key] = float(value)
            elif key == 'Timestamp':
                row[key] = float(value)  # Assuming timestamp is in Excel format
        except ValueError:
            pass  # Handle or log the error as needed
    return row


def csv_to_line_protocol(csv_file_path, measurement):
    """
    Convert CSV data to line protocol format.

    Args:
        csv_file_path (str): Path to the CSV file.
        measurement (str): Measurement name for the line protocol.

    Returns:
        list: A list of strings, each representing a line in line protocol format.
    """
    lines = [
        "# DDL",
        "CREATE DATABASE BikeComputer\n",
        "# DML",
        "# CONTEXT-DATABASE: BikeComputer",
        "# CONTEXT-RETENTION-POLICY: autogen\n"
    ]

    start_distance = None

    try:
        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                converted_row = convert_csv_values(row)

                # Set start distance based on the first valid entry
                if start_distance is None:
                    start_distance = converted_row['distance']

                # Adjust the distance
                converted_row['distance'] -= start_distance

                # Convert timestamp and create line protocol format
                timestamp = excel_timestamp_to_datetime(converted_row['Timestamp'])
                tags = ''  # Placeholder for tags
                fields = ','.join(
                    f"{key}={value}" for key, value in converted_row.items()
                    if key != 'Timestamp' and value is not None
                )

                line = f"{measurement}{tags} {fields} {int(timestamp.timestamp())}"
                lines.append(line)
    except Exception as e:
        print(f"Error processing file: {e}")

    return lines