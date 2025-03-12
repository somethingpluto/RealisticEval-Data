import pandas as pd


def tsv_to_jsonl(tsv_file: str, jsonl_file: str):
    df = pd.read_csv(tsv_file, sep='\t')
    df.to_json(jsonl_file, orient='records', lines=True)
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