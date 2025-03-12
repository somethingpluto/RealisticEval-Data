import csv
import sys

def read_tsv_from_stdin():
    rows = []
    for line in sys.stdin:
        row = line.strip().split('\t')
        rows.append(row)
    
    max_length = max(len(row) for row in rows)
    for row in rows:
        if len(row) < max_length:
            row.extend([''] * (max_length - len(row)))
    
    return rows
import unittest
import sys
import io
from unittest.mock import patch


class TestReadTsvFromStdin(unittest.TestCase):

    @patch('sys.stdin', new_callable=io.StringIO)
    def test_basic_tsv_input(self, mock_stdin):
        mock_stdin.write("col1\tcol2\tcol3\nval1\tval2\tval3\n")
        mock_stdin.seek(0)  # Move to the start of the StringIO object
        expected_output = [['col1', 'col2', 'col3'], ['val1', 'val2', 'val3']]
        self.assertEqual(read_tsv_from_stdin(), expected_output)


    @patch('sys.stdin', new_callable=io.StringIO)
    def test_single_column(self, mock_stdin):
        mock_stdin.write("col1\nval1\nval2\n")
        mock_stdin.seek(0)
        expected_output = [['col1'], ['val1'], ['val2']]
        self.assertEqual(read_tsv_from_stdin(), expected_output)

if __name__ == '__main__':
    unittest.main()