import re


def extract_log_levels(log_file_path, output_file_path):
    # Define the regex pattern to match log levels
    log_pattern = re.compile(r'\[(WARNING|ERROR|CRITICAL|ALERT)\]')

    with open(log_file_path, 'r') as file:
        with open(output_file_path, 'w') as output:
            # Iterate over each line in the log file
            for line in file:
                # Check if the line contains any of the log levels
                if log_pattern.search(line):
                    # If it does, write this line to the output file
                    output.write(line)

import unittest
import tempfile
import os


# Assuming the extract_log_levels function is defined here or imported

class TestLogExtraction(unittest.TestCase):
    def create_temp_log_file(self, content):
        # Create a temporary log file
        temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w+')
        temp_file.write(content)
        temp_file.close()
        return temp_file.name

    def read_output_file(self, file_path):
        # Read content from a file
        with open(file_path, 'r') as file:
            return file.read()

    def test_warning_level(self):
        logs = """[INFO] Information message
[WARNING] Warning message
[DEBUG] Debug message"""
        expected_output = "[WARNING] Warning message\n"

        log_file_path = self.create_temp_log_file(logs)
        output_file_path = tempfile.NamedTemporaryFile(delete=False).name

        extract_log_levels(log_file_path, output_file_path)

        result = self.read_output_file(output_file_path)
        self.assertEqual(result, expected_output)

        os.unlink(log_file_path)
        os.unlink(output_file_path)

    def test_error_level(self):
        logs = """[ERROR] Error occurred
[INFO] Just an info"""
        expected_output = "[ERROR] Error occurred\n"

        log_file_path = self.create_temp_log_file(logs)
        output_file_path = tempfile.NamedTemporaryFile(delete=False).name

        extract_log_levels(log_file_path, output_file_path)

        result = self.read_output_file(output_file_path)
        self.assertEqual(result, expected_output)

        os.unlink(log_file_path)
        os.unlink(output_file_path)

    def test_critical_and_alert_levels(self):
        logs = """[ALERT] Security breach
[CRITICAL] System failure
[NOTICE] Something to notice"""
        expected_output = "[ALERT] Security breach\n[CRITICAL] System failure\n"

        log_file_path = self.create_temp_log_file(logs)
        output_file_path = tempfile.NamedTemporaryFile(delete=False).name

        extract_log_levels(log_file_path, output_file_path)

        result = self.read_output_file(output_file_path)
        self.assertEqual(result, expected_output)

        os.unlink(log_file_path)
        os.unlink(output_file_path)

    def test_no_relevant_logs(self):
        logs = "[INFO] No issues here\n[DEBUG] All systems go"
        expected_output = ""

        log_file_path = self.create_temp_log_file(logs)
        output_file_path = tempfile.NamedTemporaryFile(delete=False).name

        extract_log_levels(log_file_path, output_file_path)

        result = self.read_output_file(output_file_path)
        self.assertEqual(result, expected_output)

        os.unlink(log_file_path)
        os.unlink(output_file_path)

    def test_mixed_logs(self):
        logs = """[WARNING] Low disk space
[INFO] Update completed
[ERROR] Failed to load module
[CRITICAL] Memory leak detected
[DEBUG] This is a debug message"""
        expected_output = "[WARNING] Low disk space\n[ERROR] Failed to load module\n[CRITICAL] Memory leak detected\n"

        log_file_path = self.create_temp_log_file(logs)
        output_file_path = tempfile.NamedTemporaryFile(delete=False).name

        extract_log_levels(log_file_path, output_file_path)

        result = self.read_output_file(output_file_path)
        self.assertEqual(result, expected_output)

        os.unlink(log_file_path)
        os.unlink(output_file_path)

if __name__ == '__main__':
    unittest.main()