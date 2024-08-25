import unittest
from unittest.mock import mock_open, patch, MagicMock
import json


class TestConvertTsvToJsonl(unittest.TestCase):
    def setUp(self):
        # Example TSV content
        self.tsv_content = "Name\tAge\tCity\nJohn Doe\t28\tNew York\nJane Smith\t32\tLos Angeles"
        # Expected JSONL output for selective columns
        self.jsonl_content = json.dumps({"Name": "John Doe", "City": "New York"}) + "\n" + \
                             json.dumps({"Name": "Jane Smith", "City": "Los Angeles"}) + "\n"

    @patch("builtins.open", new_callable=mock_open, read_data="Name\tAge\tCity\nJohn Doe\t28\tNew York")
    def test_correct_conversion(self, mock_file):
        # Test correct conversion from TSV to JSONL with selected columns
        convert_tsv_to_jsonl('fake_tsv.tsv', 'fake_jsonl.jsonl', ['Name', 'City'])
        mock_file().write.assert_called_with(self.jsonl_content)

    @patch("builtins.open", new_callable=mock_open, read_data="Name\tAge\tCity\n")
    def test_empty_data(self, mock_file):
        # Test conversion when there's no data, only headers
        convert_tsv_to_jsonl('fake_tsv.tsv', 'fake_jsonl.jsonl', ['Name', 'City'])
        mock_file().write.assert_called_once_with('')

    @patch("builtins.open", mock_open(read_data="Name\tAge\tCity\nJohn Doe\t28\tNew York"))
    def test_key_error_for_missing_column(self, mock_file):
        # Test raising KeyError if a column in the list doesn't exist in the TSV file
        with self.assertRaises(KeyError):
            convert_tsv_to_jsonl('fake_tsv.tsv', 'fake_jsonl.jsonl', ['Name', 'City', 'Occupation'])

    @patch("builtins.open", new_callable=mock_open, read_data="Name\tAge\tCity\nJohn Doe\t28\tNew York")
    def test_jsonl_output_format(self, mock_file):
        # Test the format of the JSONL output
        with patch("builtins.open", mock_open()) as mocked_file:
            convert_tsv_to_jsonl('fake_tsv.tsv', 'fake_jsonl.jsonl', ['Name', 'City'])
            handle = mocked_file()
            handle.write.assert_called_with(self.jsonl_content)

    @patch("builtins.open", new_callable=mock_open, read_data="Name\tAge\tCity\nJohn Doe\t28\tNew York")
    def test_conversion_with_all_columns(self, mock_file):
        # Test conversion using all available columns
        jsonl_all_cols_content = json.dumps({"Name": "John Doe", "Age": "28", "City": "New York"}) + "\n"
        convert_tsv_to_jsonl('fake_tsv.tsv', 'fake_jsonl.jsonl', ['Name', 'Age', 'City'])
        mock_file().write.assert_called_with(jsonl_all_cols_content)
