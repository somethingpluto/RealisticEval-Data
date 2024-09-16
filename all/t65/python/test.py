import unittest
from unittest.mock import mock_open, patch


class TestFindDuplicateIps(unittest.TestCase):
    def setUp(self):
        self.files = ["file1.txt", "file2.txt", "file3.txt"]
        self.ignored_ips = {"192.168.1.1", "10.0.0.2"}

    @patch('os.path.isfile')
    @patch('builtins.open', new_callable=mock_open, read_data="192.168.0.1\n192.168.1.1\n192.168.0.1\n")
    def test_duplicates_with_ignored(self, mock_file, mock_isfile):
        # Setup
        mock_isfile.return_value = True
        expected_result = {'192.168.0.1': ['file1.txt']}

        # Execution
        result = find_duplicate_ips(self.files[:1], self.ignored_ips)

        # Assertion
        self.assertEqual(result, expected_result)

    @patch('os.path.isfile')
    @patch('builtins.open', new_callable=mock_open, read_data="192.168.0.1\n192.168.0.1\n")
    def test_single_file_duplicates(self, mock_file, mock_isfile):
        mock_isfile.return_value = True
        expected_result = {'192.168.0.1': ['file1.txt']}
        result = find_duplicate_ips(self.files[:1], set())
        self.assertEqual(result, expected_result)

    @patch('os.path.isfile')
    def test_non_existent_file(self, mock_isfile):
        mock_isfile.return_value = False
        result = find_duplicate_ips(["nonexistent.txt"], self.ignored_ips)
        self.assertEqual(result, {})

    @patch('os.path.isfile')
    @patch('builtins.open', new_callable=mock_open, read_data="192.168.0.1\n10.0.0.1\n192.168.0.1\n")
    def test_multiple_files_one_ignored(self, mock_file, mock_isfile):
        mock_isfile.side_effect = [True, True, True]
        expected_result = {'192.168.0.1': ['file1.txt', 'file2.txt']}
        result = find_duplicate_ips(self.files, self.ignored_ips)
        self.assertEqual(result, expected_result)

    @patch('os.path.isfile')
    @patch('builtins.open', new_callable=mock_open, read_data="192.168.0.1\n192.168.0.1\n192.168.0.1\n")
    def test_multiple_occurrences_single_file(self, mock_file, mock_isfile):
        mock_isfile.return_value = True
        expected_result = {'192.168.0.1': ['file1.txt']}
        result = find_duplicate_ips(self.files[:1], set())
        self.assertEqual(result, expected_result)
