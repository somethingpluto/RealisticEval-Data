import json
import unittest
from unittest.mock import patch, mock_open


class TestTSVToJSONL(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data="name\tage\nAlice\t30\nBob\t25")
    def test_normal_case(self, mock_open_func):
        tsv_file_path = "dummy.tsv"
        jsonl_file_path = "dummy.jsonl"
        expected_output = [
            json.dumps({"name": "Alice", "age": "30"}) + "\n",
            json.dumps({"name": "Bob", "age": "25"}) + "\n"
        ]

        with patch('builtins.open', mock_open()) as mocked_file:
            tsv_to_jsonl(tsv_file_path, jsonl_file_path)
            mocked_file().write.assert_called_with(expected_output[-1])  # Last call is checked

    @patch('builtins.open', new_callable=mock_open, read_data="")
    def test_empty_tsv_file(self, mock_open_func):
        tsv_file_path = "dummy.tsv"
        jsonl_file_path = "dummy.jsonl"

        with patch('builtins.open', mock_open()) as mocked_file:
            tsv_to_jsonl(tsv_file_path, jsonl_file_path)
            mocked_file().write.assert_not_called()  # No write call should be made

    @patch('builtins.open', new_callable=mock_open,
           read_data="name\tquote\nJohn\t\"Life is\nbeautiful\"\nJane\t\"Enjoy, life!\"")
    def test_special_characters(self, mock_open_func):
        tsv_file_path = "dummy.tsv"
        jsonl_file_path = "dummy.jsonl"
        expected_output = [
            json.dumps({"name": "John", "quote": "Life is\nbeautiful"}) + "\n",
            json.dumps({"name": "Jane", "quote": "Enjoy, life!"}) + "\n"
        ]

        with patch('builtins.open', mock_open()) as mocked_file:
            tsv_to_jsonl(tsv_file_path, jsonl_file_path)
            mocked_file().write.assert_called_with(expected_output[-1])  # Last call is checked

    @patch('builtins.open', new_callable=mock_open, read_data="name\tage\nAlice\t30")
    def test_single_row_tsv_file(self, mock_open_func):
        tsv_file_path = "dummy.tsv"
        jsonl_file_path = "dummy.jsonl"
        expected_output = json.dumps({"name": "Alice", "age": "30"}) + "\n"

        with patch('builtins.open', mock_open()) as mocked_file:
            tsv_to_jsonl(tsv_file_path, jsonl_file_path)
            mocked_file().write.assert_called_with(expected_output)

    @patch('builtins.open', new_callable=mock_open, read_data="name\tage\nAlice\t30\nBob\t")
    def test_missing_columns(self, mock_open_func):
        tsv_file_path = "dummy.tsv"
        jsonl_file_path = "dummy.jsonl"
        expected_output = [
            json.dumps({"name": "Alice", "age": "30"}) + "\n",
            json.dumps({"name": "Bob", "age": ""}) + "\n"
        ]

        with patch('builtins.open', mock_open()) as mocked_file:
            tsv_to_jsonl(tsv_file_path, jsonl_file_path)
            mocked_file().write.assert_called_with(expected_output[-1])  # Last call is checked
import csv
import json


def tsv_to_jsonl(tsv_file_path: str, jsonl_file_path: str) -> None:
    """
    Convert a TSV file to a JSONL file.

    Parameters:
    - tsv_file_path (str): Path to the input TSV file.
    - jsonl_file_path (str): Path to the output JSONL file.
    """
    try:
        with open(tsv_file_path, 'r', newline='', encoding='utf-8') as tsv_file, \
                open(jsonl_file_path, 'w', encoding='utf-8') as jsonl_file:

            # Create a CSV reader object using the tab delimiter
            tsv_reader = csv.DictReader(tsv_file, delimiter='\t')

            # Write each row as a JSON object to the JSONL file
            for row in tsv_reader:
                jsonl_file.write(json.dumps(row) + '\n')

        print(f"Successfully converted {tsv_file_path} to {jsonl_file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")