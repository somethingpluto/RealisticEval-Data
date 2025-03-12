
import pandas as pd

def tsv_to_jsonl(tsv_file: str, jsonl_file: str):
    # Read the contents of the tsv file as a Pandas DataFrame
    df = pd.read_csv(tsv_file)
    
    # Write the DataFrame to a JSON object
    json_df = {'data': df.to_json()}
    
    # Write the JSON object to the jsonl file
    with open(jsonl_file, 'w') as f:
        f.write(json_df)

tsv_to_jsonl('path/to/tsv/file.csv', 'path/to/jsonl/file.json')

import os
import tempfile
import unittest


class TestTSVtoJSONL(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        # Clean up the temporary directory
        self.test_dir.cleanup()

    def test_standard_tsv(self):
        tsv_content = "Name\tAge\tCountry\nAlice\t30\tUSA\nBob\t25\tCanada\n"
        tsv_file = os.path.join(self.test_dir.name, 'test_standard.tsv')
        jsonl_file = os.path.join(self.test_dir.name, 'test_standard.jsonl')

        with open(tsv_file, 'w', encoding='utf-8') as f:
            f.write(tsv_content)

        tsv_to_jsonl(tsv_file, jsonl_file)

        with open(jsonl_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        expected_lines = [
            '{"Name":"Alice","Age":30,"Country":"USA"}\n',
            '{"Name":"Bob","Age":25,"Country":"Canada"}\n'
        ]
        self.assertEqual(lines, expected_lines)


    def test_single_row_tsv(self):
        tsv_content = "Name\tAge\tCountry\nAlice\t30\tUSA\n"
        tsv_file = os.path.join(self.test_dir.name, 'test_single_row.tsv')
        jsonl_file = os.path.join(self.test_dir.name, 'test_single_row.jsonl')

        with open(tsv_file, 'w', encoding='utf-8') as f:
            f.write(tsv_content)

        tsv_to_jsonl(tsv_file, jsonl_file)

        with open(jsonl_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        expected_lines = [
            '{"Name":"Alice","Age":30,"Country":"USA"}\n'
        ]
        self.assertEqual(lines, expected_lines)

    def test_numeric_and_boolean_values(self):
        tsv_content = "Name\tAge\tIs_Student\nAlice\t30\tTrue\nBob\t25\tFalse\n"
        tsv_file = os.path.join(self.test_dir.name, 'test_numeric_boolean.tsv')
        jsonl_file = os.path.join(self.test_dir.name, 'test_numeric_boolean.jsonl')

        with open(tsv_file, 'w', encoding='utf-8') as f:
            f.write(tsv_content)

        tsv_to_jsonl(tsv_file, jsonl_file)

        with open(jsonl_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        expected_lines = [
            '{"Name":"Alice","Age":30,"Is_Student":true}\n',
            '{"Name":"Bob","Age":25,"Is_Student":false}\n'
        ]
        self.assertEqual(lines, expected_lines)

if __name__ == '__main__':
    unittest.main()