import unittest
from io import StringIO
from unittest.mock import patch, mock_open
from task_code.t2.adapted import print_binary_from_file


class TestPrintBinaryFromFile(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data=b'\xd5\x69')
    @patch('sys.stdout', new_callable=StringIO)
    def test_normal_case(self, mock_stdout, mock_file):
        print_binary_from_file('dummy.bin', 8)
        self.assertEqual(mock_stdout.getvalue(), '1101010101101001\n')

    @patch('builtins.open', new_callable=mock_open, read_data=b'\x05')
    @patch('sys.stdout', new_callable=StringIO)
    def test_incomplete_width(self, mock_stdout, mock_file):
        print_binary_from_file('dummy.bin', 5)
        self.assertEqual(mock_stdout.getvalue(), '00000\n0101\n')

    @patch('builtins.open', side_effect=IOError)
    @patch('sys.stdout', new_callable=StringIO)
    def test_file_not_found(self, mock_stdout, mock_file):
        print_binary_from_file('nonexistent.bin', 8)
        self.assertEqual(mock_stdout.getvalue(), 'Error: File not found or cannot be read.\n')

    @patch('builtins.open', new_callable=mock_open, read_data=b'')
    @patch('sys.stdout', new_callable=StringIO)
    def test_empty_file(self, mock_stdout, mock_file):
        print_binary_from_file('empty.bin', 8)
        self.assertEqual(mock_stdout.getvalue(), '')

    @patch('builtins.open', new_callable=mock_open, read_data=b'\xd5\x69')
    @patch('sys.stdout', new_callable=StringIO)
    def test_zero_width(self, mock_stdout, mock_file):
        print_binary_from_file('dummy.bin', 0)
        self.assertEqual(mock_stdout.getvalue(), '')  # Assuming no output for zero width as per design choice.
