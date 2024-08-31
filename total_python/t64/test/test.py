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
