import unittest
import json
import os
from tempfile import NamedTemporaryFile


class TestClassifyJsonObjectsByPid(unittest.TestCase):
    def setUp(self):
        # Create a temporary file to write the source JSON data
        self.source_file = NamedTemporaryFile(delete=False, mode='w', suffix='.json',encoding="utf8")
        self.source_file_name = self.source_file.name

        # Create temporary files for match and mismatch results
        self.match_file = NamedTemporaryFile(delete=False, mode='w+', suffix='.json',encoding="utf8")
        self.match_file_name = self.match_file.name
        self.mismatch_file = NamedTemporaryFile(delete=False, mode='w+', suffix='.json',encoding="utf8")
        self.mismatch_file_name = self.mismatch_file.name

        # Example data
        self.data = [
            {"pid": 123, "name": "Alice"},
            {"pid": 456, "name": "Bob"},
            {"pid": 789, "name": "Charlie"},
            {"pid": 101, "name": "Dave"},
            {"pid": 102, "name": "Eve"}
        ]

        # Write the example data to the source file
        json.dump(self.data, self.source_file)
        self.source_file.close()

        # PID list for testing
        self.pid_list = [123, 789, 456]

    def tearDown(self):
        # Clean up temporary files
        os.unlink(self.source_file_name)
        os.unlink(self.match_file_name)
        os.unlink(self.mismatch_file_name)

    def test_all_matches(self):
        # All items should match
        classify_json_objects_by_pid(self.source_file_name, [123, 456, 789, 101, 102], self.match_file_name,
                                     self.mismatch_file_name)
        with open(self.match_file_name, 'r',encoding="utf8") as f:
            results = json.load(f)
        self.assertEqual(len(results), 5)
        self.assertEqual(results, self.data)

    def test_no_matches(self):
        # No items should match
        classify_json_objects_by_pid(self.source_file_name, [], self.match_file_name, self.mismatch_file_name)
        with open(self.mismatch_file_name, 'r',encoding="utf8") as f:
            results = json.load(f)
        self.assertEqual(len(results), 5)
        self.assertEqual(results, self.data)

    def test_partial_matches(self):
        # Only some items should match
        classify_json_objects_by_pid(self.source_file_name, self.pid_list, self.match_file_name,
                                     self.mismatch_file_name)
        with open(self.match_file_name, 'r',encoding="utf8") as f:
            match_results = json.load(f)
        with open(self.mismatch_file_name, 'r',encoding="utf8") as f:
            mismatch_results = json.load(f)
        self.assertEqual(len(match_results), 3)
        self.assertEqual(len(mismatch_results), 2)

    def test_empty_source(self):
        # Test with an empty source file
        with open(self.source_file_name, 'w') as f:
            json.dump([], f)
        classify_json_objects_by_pid(self.source_file_name, self.pid_list, self.match_file_name,
                                     self.mismatch_file_name)
        with open(self.match_file_name, 'r',encoding="utf8") as f:
            match_results = json.load(f)
        with open(self.mismatch_file_name, 'r',encoding="utf8") as f:
            mismatch_results = json.load(f)
        self.assertEqual(len(match_results), 0)
        self.assertEqual(len(mismatch_results), 0)

    def test_invalid_pid_list(self):
        # Test with an invalid pid list (non-matching types)
        classify_json_objects_by_pid(self.source_file_name, ['123', '789', '456'], self.match_file_name,
                                     self.mismatch_file_name)
        with open(self.match_file_name, 'r',encoding="utf8") as f:
            match_results = json.load(f)
        self.assertEqual(len(match_results), 0)  # Assumes no conversion between types

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