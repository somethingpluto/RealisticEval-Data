import re

def extract_log_entries(log_file_path:str):
    with open(log_file_path, 'r') as file:
        log_entries = file.readlines()
    
    warning_entries = []
    error_entries = []
    critical_entries = []
    alert_entries = []
    
    for entry in log_entries:
        if re.search(r'\bWARNING\b', entry):
            warning_entries.append(entry)
        elif re.search(r'\bERROR\b', entry):
            error_entries.append(entry)
        elif re.search(r'\bCRITICAL\b', entry):
            critical_entries.append(entry)
        elif re.search(r'\bALERT\b', entry):
            alert_entries.append(entry)
    
    with open('warning_log_entries.txt', 'w') as file:
        for entry in warning_entries:
            file.write(entry)
    
    with open('error_log_entries.txt', 'w') as file:
        for entry in error_entries:
            file.write(entry)
    
    with open('critical_log_entries.txt', 'w') as file:
        for entry in critical_entries:
            file.write(entry)
    
    with open('alert_log_entries.txt', 'w') as file:
        for entry in alert_entries:
            file.write(entry)
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