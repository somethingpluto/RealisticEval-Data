import unittest
from unittest.mock import patch, mock_open


class TestCsvToLineProtocol(unittest.TestCase):
    # Mock CSV content
    mock_csv_data = """Timestamp,distance,speed
41895.0,0,10
41895.1,5,15
41895.2,10,20
"""
    # Expected line protocol output
    expected_lines = [
        "# DDL",
        "CREATE DATABASE BikeComputer\n",
        "# DML",
        "# CONTEXT-DATABASE: BikeComputer",
        "# CONTEXT-RETENTION-POLICY: autogen\n",
        "BikeMetrics  distance=0.0,speed=10 1420070400",
        "BikeMetrics  distance=5.0,speed=15 1420070460",
        "BikeMetrics  distance=10.0,speed=20 1420070520"
    ]

    @patch('builtins.open', new_callable=mock_open, read_data=mock_csv_data)
    @patch('your_module.csv.DictReader')
    def test_normal_case(self, mock_csv_reader, mock_file):
        # Configure the mock to return a custom iterator
        mock_csv_reader.return_value.__iter__.return_value = iter([
            {"Timestamp": "41895.0", "distance": "0", "speed": "10"},
            {"Timestamp": "41895.1", "distance": "5", "speed": "15"},
            {"Timestamp": "41895.2", "distance": "10", "speed": "20"}
        ])
        result = csv_to_line_protocol('dummy_path.csv', 'BikeMetrics')
        self.assertEqual(result, self.expected_lines)

    @patch('builtins.open', new_callable=mock_open, read_data=mock_csv_data)
    def test_file_not_found_error(self, mock_file):
        # Test handling of file not found error
        mock_file.side_effect = FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            csv_to_line_protocol('nonexistent_path.csv', 'BikeMetrics')

    @patch('builtins.open', new_callable=mock_open, read_data="")
    @patch('your_module.csv.DictReader')
    def test_empty_csv(self, mock_csv_reader, mock_file):
        # Test empty CSV handling
        mock_csv_reader.return_value.__iter__.return_value = iter([])
        result = csv_to_line_protocol('dummy_path.csv', 'BikeMetrics')
        self.assertEqual(result, self.expected_lines[:5])  # Only headers should be returned

    @patch('builtins.open', new_callable=mock_open, read_data=mock_csv_data)
    @patch('your_module.csv.DictReader')
    def test_invalid_data_types(self, mock_csv_reader, mock_file):
        # Test handling of invalid data types
        mock_csv_reader.return_value.__iter__.return_value = iter([
            {"Timestamp": "invalid", "distance": "not_a_number", "speed": "ten"}
        ])
        result = csv_to_line_protocol('dummy_path.csv', 'BikeMetrics')
        self.assertEqual(result, self.expected_lines[:5])  # Expect headers only due to conversion failure

    @patch('builtins.open', new_callable=mock_open, read_data=mock_csv_data)
    @patch('your_module.csv.DictReader')
    def test_all_records_invalid(self, mock_csv_reader, mock_file):
        # Test with all records being invalid
        mock_csv_reader.return_value.__iter__.return_value = iter([
            {"Timestamp": "0", "distance": "-1", "speed": "20"},  # Invalid timestamp and distance
            {"Timestamp": "41895.1", "distance": "5", "speed": "none"}  # Invalid speed
        ])
        result = csv_to_line_protocol('dummy_path.csv', 'BikeMetrics')
        self.assertEqual(result, self.expected_lines[:5])  # Only headers due to all invalid data

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