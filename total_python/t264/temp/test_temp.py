import unittest
import os


class TestExtractLogEntries(unittest.TestCase):

    def setUp(self):
        """Setup a temporary log file with sample data for testing."""
        self.log_file_path = 'test_log.log'
        self.log_contents = [
            "INFO: This is an informational message.\n",
            "WARNING: This is a warning message.\n",
            "ERROR: This is an error message.\n",
            "CRITICAL: This is a critical message.\n",
            "ALERT: This is an alert message.\n"
        ]
        with open(self.log_file_path, 'w') as log_file:
            log_file.writelines(self.log_contents)

    def tearDown(self):
        """Clean up by removing files created during the test."""
        os.remove(self.log_file_path)
        for level in ['WARNING', 'ERROR', 'CRITICAL', 'ALERT']:
            os.remove(f"{level.lower()}_logs.txt")

    def test_extract_all_levels(self):
        """Test extracting logs for all specified levels."""
        extract_log_entries(self.log_file_path)
        # Check for each level's output file
        for level in ['WARNING', 'ERROR', 'CRITICAL', 'ALERT']:
            with open(f"{level.lower()}_logs.txt", 'r') as file:
                self.assertEqual(file.readline(), f"{level}: This is a {level.lower()} message.\n")

    def test_no_logs_of_certain_levels(self):
        """Test the situation where there are no log entries for one or more levels."""
        with open(self.log_file_path, 'w') as log_file:
            log_file.write("INFO: This is another informational message.\n")
        extract_log_entries(self.log_file_path)
        for level in ['WARNING', 'ERROR', 'CRITICAL', 'ALERT']:
            with open(f"{level.lower()}_logs.txt", 'r') as file:
                self.assertEqual('', file.read())

    def test_file_not_found(self):
        """Test behavior when the log file does not exist."""
        with self.assertRaises(FileNotFoundError):
            extract_log_entries("nonexistent.log")

    def test_empty_log_file(self):
        """Test behavior with an empty log file."""
        with open(self.log_file_path, 'w') as log_file:
            log_file.write("")
        extract_log_entries(self.log_file_path)
        for level in ['WARNING', 'ERROR', 'CRITICAL', 'ALERT']:
            with open(f"{level.lower()}_logs.txt", 'r') as file:
                self.assertEqual('', file.read())

    def test_mixed_content_log_file(self):
        """Test extracting logs from a file with mixed content."""
        with open(self.log_file_path, 'w') as log_file:
            log_file.writelines([
                "INFO: Some info.\n",
                "WARNING: Watch out!\n",
                "DEBUG: Debugging.\n",
                "ERROR: Oops!\n",
                "CRITICAL: Failed badly.\n",
                "ALERT: High alert!\n",
                "INFO: More info.\n"
            ])
        extract_log_entries(self.log_file_path)
        for level in ['WARNING', 'ERROR', 'CRITICAL', 'ALERT']:
            with open(f"{level.lower()}_logs.txt", 'r') as file:
                content = file.read().strip()
                self.assertIn(level, content)

import os


def extract_log_entries(log_file_path):
    """
    Extract log entries from a log file for WARNING, ERROR, CRITICAL, and ALERT levels
    and save each type of log entry to a different file.

    Args:
    log_file_path (str): Path to the log file.
    """
    if not os.path.exists(log_file_path):
        raise FileNotFoundError(f"No log file found at the specified path: {log_file_path}")

    # Prepare dictionaries to hold log entries for each level
    logs = {
        'WARNING': [],
        'ERROR': [],
        'CRITICAL': [],
        'ALERT': []
    }

    # Define output file paths
    output_files = {
        'WARNING': 'warning_logs.txt',
        'ERROR': 'error_logs.txt',
        'CRITICAL': 'critical_logs.txt',
        'ALERT': 'alert_logs.txt'
    }

    # Read the log file and filter entries by level
    with open(log_file_path, 'r') as file:
        for line in file:
            for level in logs.keys():
                if level in line:
                    logs[level].append(line)
                    break

    # Write the filtered logs to separate files
    for level, entries in logs.items():
        with open(output_files[level], 'w') as outfile:
            outfile.writelines(entries)
            print(f"Saved {len(entries)} '{level}' entries to {output_files[level]}.")