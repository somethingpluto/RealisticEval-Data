import unittest
from unittest.mock import patch, mock_open

import pandas as pd


class TestCSVToLineProtocol(unittest.TestCase):

    def setUp(self):
        # Example data to be used across tests
        self.example_data = """measurement,tag_key,field_key,value,timestamp
                                weather,location=us-midwest temperature,82,1597689110
                                energy,source=solar voltage,12.1,1597689110"""

    @patch('builtins.open', new_callable=mock_open)
    @patch('pandas.read_csv')
    def test_basic_conversion(self, mock_read_csv, mock_file):
        # Setup mock
        df = pd.read_csv(pd.compat.StringIO(self.example_data))
        mock_read_csv.return_value = df

        # Run the function
        csv_to_line_protocol('dummy.csv', 'output.lp')

        # Check if the output is written correctly
        mock_file().write.assert_called_with("weather,location=us-midwest temperature=82 1597689110\n")

    @patch('pandas.read_csv')
    def test_empty_csv_file(self, mock_read_csv):
        # Setup empty DataFrame
        mock_read_csv.return_value = pd.DataFrame()

        # Check if ValueError is raised
        with self.assertRaises(ValueError):
            csv_to_line_protocol('empty.csv', 'output.lp')

    @patch('pandas.read_csv')
    def test_invalid_csv_format(self, mock_read_csv):
        # DataFrame missing 'measurement' column
        data = """tag_key,field_key,value,timestamp
                  location=us-midwest,temperature,82,1597689110"""
        df = pd.read_csv(pd.compat.StringIO(data))
        mock_read_csv.return_value = df

        with self.assertRaises(KeyError):
            csv_to_line_protocol('invalid.csv', 'output.lp')

    @patch('builtins.open', new_callable=mock_open)
    @patch('pandas.read_csv')
    def test_special_characters(self, mock_read_csv, mock_file):
        # Data with special characters
        data = """measurement,tag_key,field_key,value,timestamp
                  weather,location=us, midwest temperature,82.5,1597689110"""
        df = pd.read_csv(pd.compat.StringIO(data))
        mock_read_csv.return_value = df

        csv_to_line_protocol('special.csv', 'output.lp')

        # Check if special characters are handled
        mock_file().write.assert_called_with("weather,location=us, midwest temperature=82.5 1597689110\n")

    @patch('builtins.open', new_callable=mock_open)
    @patch('pandas.read_csv')
    def test_large_csv_file(self, mock_read_csv, mock_file):
        # Simulating a large CSV by repeating example data
        large_data = self.example_data * 100  # Repeat data 100 times
        df = pd.read_csv(pd.compat.StringIO(large_data))
        mock_read_csv.return_value = df

        csv_to_line_protocol('large.csv', 'output.lp')

        # Assert that the file write function was called 100 times
        self.assertEqual(mock_file().write.call_count, 100)
