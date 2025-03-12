import os

def extract_log_entries(log_file_path:str):
    warning_file = "warning_log.txt"
    error_file = "error_log.txt"
    critical_file = "critical_log.txt"
    alert_file = 'alert_log.txt'

    with open(log_file_path, "r") as log_file:
        warning_logs = []
        error_logs = []
        critical_logs = []
        alert_logs = []

        for line in log_file:
            if "WARNING" in line:
                warning_logs.append(line)
            elif "ERROR" in line:
                error_logs.append(line)
            elif "CRITICAL" in line:
                critical_logs.append(line)
            elif "ALERT" in line:
                alert_logs.append(line)

    with open(warning_file, "w") as file:
        for log in warning_logs:
            file.write(log)

    with open(error_file, "w") as file:
        for log in error_logs:
            file.write(log)

    with open(critical_file, "w") as file:
        for log in critical_logs:
            file.write(log)

    with open(alert_file, "w") as file:
        for log in alert_logs:
            file.write(log)
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