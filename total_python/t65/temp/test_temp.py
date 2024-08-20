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
    @patch('builtins.open', new_callable=mock_open, read_data="192.168.0.1\n192.168.0.1\n192.168.0.1\n")
    def test_multiple_occurrences_single_file(self, mock_file, mock_isfile):
        mock_isfile.return_value = True
        expected_result = {'192.168.0.1': ['file1.txt']}
        result = find_duplicate_ips(self.files[:1], set())
        self.assertEqual(result, expected_result)

import os
import re


def find_duplicate_ips(files, ignored_ips):
    """
    Find duplicate IP addresses across multiple files, excluding any IPs in the ignored list.

    Args:
    files (list): List of file paths to search.
    ignored_ips (set): Set of IP addresses to ignore.

    Returns:
    dict: A dictionary where each key is a duplicated IP address and the value is a list of filenames where the IP appears.
    """
    ip_regex = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    duplicates = {}

    for filename in files:
        # Check if the file exists before attempting to open
        if not os.path.isfile(filename):
            print(f"Skipping non-existent file: {filename}")
            continue

        with open(filename, "r") as file:
            for line in file:
                ips = re.findall(ip_regex, line)
                for ip in ips:
                    # Skip any IPs that are in the ignored list
                    if ip in ignored_ips:
                        continue

                    if ip not in duplicates:
                        duplicates[ip] = {filename}
                    else:
                        duplicates[ip].add(filename)

    # Convert sets to lists for consistent output
    return {ip: list(files) for ip, files in duplicates.items()}