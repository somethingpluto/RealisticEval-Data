import unittest
from unittest.mock import mock_open, patch

class TestConvertTSVtoJsonl(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data="premise\thypothesis\tlabel\nData1\tData2\tLabel1\nData3\tData4\tLabel2")
    @patch('json.dumps', side_effect=lambda x: str(x))  # Mock json.dumps for simplicity in assertion
    def test_correct_conversion(self, mock_json_dumps, mock_file):
        """ Test converting a correctly formatted TSV to JSONL """
        convert_tsv_to_jsonl('dummy.tsv', 'dummy.jsonl', ['premise', 'hypothesis', 'label'])
        handle = mock_file()
        handle.write.assert_any_call("{'premise': 'Data1', 'hypothesis': 'Data2', 'label': 'Label1'}\n")
        handle.write.assert_any_call("{'premise': 'Data3', 'hypothesis': 'Data4', 'label': 'Label2'}\n")

    @patch('builtins.open', new_callable=mock_open, read_data="premise\thypothesis\tlabel\nData1\tData2\tLabel1\n")
    def test_missing_column(self, mock_file):
        """ Test with a missing column specification """
        with self.assertRaises(KeyError):
            convert_tsv_to_jsonl('dummy.tsv', 'dummy.jsonl', ['premise', 'hypothesis', 'nonexistent'])

    @patch('builtins.open', new_callable=mock_open, read_data="premise hypothesis label\nData1 Data2 Label1\n")
    def test_malformed_tsv(self, mock_file):
        """ Test a malformed TSV with spaces instead of tabs """
        with self.assertRaises(IndexError):
            convert_tsv_to_jsonl('dummy.tsv', 'dummy.jsonl', ['premise', 'hypothesis', 'label'])

    @patch('builtins.open', new_callable=mock_open, read_data="")
    def test_empty_tsv(self, mock_file):
        """ Test an empty TSV file """
        with self.assertRaises(IndexError):
            convert_tsv_to_jsonl('dummy.tsv', 'dummy.jsonl', ['premise', 'hypothesis', 'label'])

    @patch('builtins.open', new_callable=mock_open, read_data="premise\thypothesis\tlabel\n")
    def test_tsv_no_data(self, mock_file):
        """ Test a TSV file with headers but no data """
        convert_tsv_to_jsonl('dummy.tsv', 'dummy.jsonl', ['premise', 'hypothesis', 'label'])
        handle = mock_file()
        handle.write.assert_not_called()  # Ensure no data was written since there are no data rows
import json


def convert_tsv_to_jsonl(tsv_file_path, jsonl_file_path, columns):
    """
    Converts data from a TSV file to a JSONL file based on specified columns.

    Args:
    tsv_file_path (str): The file path to the source TSV file.
    jsonl_file_path (str): The file path to the target JSONL file.
    columns (list of str): A list of column names to extract from the TSV and include in the JSONL.

    Raises:
    KeyError: If any specified column does not exist in the TSV header.
    """
    with open(tsv_file_path, 'r') as tsvfile, open(jsonl_file_path, 'w') as jsonlfile:
        # Read the header to determine column indexes
        header = tsvfile.readline().strip().split('\t')
        indexes = {column: header.index(column) for column in columns}  # Raises KeyError if column not found

        # Process each line in the TSV file
        for line in tsvfile:
            fields = line.strip().split('\t')
            # Extract the fields based on the column indexes and create a dictionary
            instance = {column: fields[indexes[column]] for column in columns}
            # Write the dictionary as a JSON string to the JSONL file
            jsonlfile.write(json.dumps(instance) + '\n')
