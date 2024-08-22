import unittest
import json
import tempfile
import os

class TestClassifyJsonObjectsByPid(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory
        self.temp_dir = tempfile.mkdtemp()

        # Create temporary files for testing
        self.source_file = os.path.join(self.temp_dir, 'source.json')
        self.match_file = os.path.join(self.temp_dir, 'match.json')
        self.mismatch_file = os.path.join(self.temp_dir, 'mismatch.json')

        # Example data
        self.data = [
            {"name": "Alice", "pid": 1},
            {"name": "Bob", "pid": 2},
            {"name": "Charlie", "pid": 3}
        ]
        self.pid_list = [1, 3]

        # Write example data to source file
        with open(self.source_file, 'w') as f:
            json.dump(self.data, f)

    def test_all_match(self):
        # Test where all items match
        classify_json_objects_by_pid(self.source_file, [1, 2, 3], self.match_file, self.mismatch_file)
        with open(self.match_file, 'r') as f:
            matches = json.load(f)
        with open(self.mismatch_file, 'r') as f:
            mismatches = json.load(f)
        self.assertEqual(len(matches), 3)
        self.assertEqual(len(mismatches), 0)

    def test_no_match(self):
        # Test where no items match
        classify_json_objects_by_pid(self.source_file, [4, 5], self.match_file, self.mismatch_file)
        with open(self.match_file, 'r') as f:
            matches = json.load(f)
        with open(self.mismatch_file, 'r') as f:
            mismatches = json.load(f)
        self.assertEqual(len(matches), 0)
        self.assertEqual(len(mismatches), 3)

    def test_partial_match(self):
        # Test where some items match
        classify_json_objects_by_pid(self.source_file, self.pid_list, self.match_file, self.mismatch_file)
        with open(self.match_file, 'r') as f:
            matches = json.load(f)
        with open(self.mismatch_file, 'r') as f:
            mismatches = json.load(f)
        self.assertEqual(len(matches), 2)
        self.assertEqual(len(mismatches), 1)

    def test_empty_pid_list(self):
        # Test with an empty PID list
        classify_json_objects_by_pid(self.source_file, [], self.match_file, self.mismatch_file)
        with open(self.match_file, 'r') as f:
            matches = json.load(f)
        with open(self.mismatch_file, 'r') as f:
            mismatches = json.load(f)
        self.assertEqual(len(matches), 0)
        self.assertEqual(len(mismatches), 3)

import json


def classify_json_objects_by_pid(source_file, pid_list, match_file, mismatch_file):
    """
    Reads JSON data from a file, filters objects based on 'pid' field inclusion in 'pid_list'.
    Writes matches and mismatches to separate JSON files.

    Args:
    source_file (str): Path to the source JSON file.
    pid_list (list): List of pids to match.
    match_file (str): Path to save matching objects JSON.
    mismatch_file (str): Path to save mismatching objects JSON.
    """
    try:

        # Load data from the source JSON file
        with open(source_file, 'r') as file:
            data = json.load(file)
        # Initialize lists for matches and mismatches
        matches = []
        mismatches = []

        # Classify each object based on 'pid' presence in 'pid_list'
        for obj in data:
            if obj.get('pid') in pid_list:
                matches.append(obj)
            else:
                mismatches.append(obj)

        # Save the matches to a new JSON file
        with open(match_file, 'w') as file:
            json.dump(matches, file, indent=4)

        # Save the mismatches to another JSON file
        with open(mismatch_file, 'w') as file:
            json.dump(mismatches, file, indent=4)

        print("Classification complete. Data saved to respective files.")

    except Exception as e:
        print(f"An error occurred: {e}")