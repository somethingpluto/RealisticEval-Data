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
        self.assertEqual(read_tsv_data_from_std_input(), expected_output)


    @patch('sys.stdin', new_callable=io.StringIO)
    def test_single_column(self, mock_stdin):
        mock_stdin.write("col1\nval1\nval2\n")
        mock_stdin.seek(0)
        expected_output = [['col1'], ['val1'], ['val2']]
        self.assertEqual(read_tsv_data_from_std_input(), expected_output)
        @patch('sys.stdin', new_callable=io.StringIO)
    

    @patch('sys.stdin', new_callable=io.StringIO)
    def test_all_rows_empty(self, mock_stdin):
        mock_stdin.write("col1\tcol2\tcol3\n\n\n")
        mock_stdin.seek(0)
        expected_output = [['col1', 'col2', 'col3'], ['', '', '']]
        self.assertEqual(read_tsv_data_from_std_input(), expected_output)

    @patch('sys.stdin', new_callable=io.StringIO)
    def test_multiple_consecutive_tabs(self, mock_stdin):
        mock_stdin.write("col1\t\tcol2\tcol3\nval1\t\tval2\tval3\n")
        mock_stdin.seek(0)
        expected_output = [['col1', '', 'col2', 'col3'], ['val1', '', 'val2', 'val3']]
        self.assertEqual(read_tsv_data_from_std_input(), expected_output)
    @patch('sys.stdin', new_callable=io.StringIO)
    def test_missing_columns(self, mock_stdin):
        mock_stdin.write("col1\tcol2\tcol3\nval1\tval2\nval1.1\tval2.1\tval3.1\n")
        mock_stdin.seek(0)
        expected_output = [['col1', 'col2', 'col3'], ['val1', 'val2'], ['val1.1', 'val2.1', 'val3.1']]
        self.assertEqual(read_tsv_data_from_std_input(), expected_output)