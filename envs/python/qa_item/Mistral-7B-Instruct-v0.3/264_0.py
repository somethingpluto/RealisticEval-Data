import re
import logzero
from logzero import logger

def extract_log_entries(log_file_path: str):
    logzero.setup_file_logger(log_file_path, level=logzero.WARNING)

    warning_log_file = f"{log_file_path.split('.')[0]}_warning.log"
    error_log_file = f"{log_file_path.split('.')[0]}_error.log"
    critical_log_file = f"{log_file_path.split('.')[0]}_critical.log"
    alert_log_file = f"{log_file_path.split('.')[0]}_alert.log"

    warning_logs = []
    error_logs = []
    critical_logs = []
    alert_logs = []

    for log in logzero.log:
        if log.levelname == "WARNING":
            warning_logs.append(log)
        elif log.levelname == "ERROR":
            error_logs.append(log)
        elif log.levelname == "CRITICAL":
            critical_logs.append(log)
        elif log.levelname == "ALERT":
            alert_logs.append(log)

    with open(warning_log_file, 'w') as f:
        for log in warning_logs:
            f.write(f"{log}\n")

    with open(error_log_file, 'w') as f:
        for log in error_logs:
            f.write(f"{log}\n")

    with open(critical_log_file, 'w') as f:
        for log in critical_logs:
            f.write(f"{log}\n")

    with open(alert_log_file, 'w') as f:
        for log in alert_logs:
            f.write(f"{log}\n")
import unittest
import os


class TestExtractLogEntries(unittest.TestCase):

    def setUp(self):
        """Setup a temporary log file with sample question for testing."""
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

if __name__ == '__main__':
    unittest.main()