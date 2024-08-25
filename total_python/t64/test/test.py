import unittest
import pandas as pd
from io import StringIO
import os


class TestCSVToLineProtocol(unittest.TestCase):

    def setUp(self):
        """Create a sample CSV file for testing."""
        self.sample_csv = StringIO("""
measurement,tag_key,field_key,value,timestamp
temperature,location=office,degrees,23.5,1625097600
humidity,location=office,percentage,40,1625097600
""")
        self.sample_csv_path = "test_input.csv"
        with open(self.sample_csv_path, 'w') as f:
            f.write(self.sample_csv.getvalue())

        self.output_path = "test_output.lp"

    def tearDown(self):
        """Clean up created files."""
        os.remove(self.sample_csv_path)
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

    def test_normal_case(self):
        """Test converting a well-formed CSV to line protocol format."""
        csv_to_line_protocol(self.sample_csv_path, self.output_path)
        with open(self.output_path, 'r') as f:
            lines = f.readlines()
        self.assertIn("temperature,location=office degrees=23.5 1625097600\n", lines)
        self.assertIn("humidity,location=office percentage=40 1625097600\n", lines)

    def test_empty_csv(self):
        """Test converting an empty CSV file."""
        empty_csv_path = "empty_test.csv"
        with open(empty_csv_path, 'w') as f:
            f.write("")
        csv_to_line_protocol(empty_csv_path, self.output_path)
        self.assertFalse(os.path.getsize(self.output_path))  # Output file should be empty
        os.remove(empty_csv_path)

    def test_incomplete_data(self):
        """Test with missing columns in the CSV."""
        incomplete_csv = StringIO("""
measurement,tag_key,field_key,value
temperature,location=office,degrees,23.5
""")
        incomplete_csv_path = "incomplete_test.csv"
        with open(incomplete_csv_path, 'w') as f:
            f.write(incomplete_csv.getvalue())
        with self.assertRaises(KeyError):
            csv_to_line_protocol(incomplete_csv_path, self.output_path)
        os.remove(incomplete_csv_path)

    def test_invalid_csv_path(self):
        """Test with an invalid CSV file path."""
        with self.assertRaises(FileNotFoundError):
            csv_to_line_protocol("nonexistent.csv", self.output_path)

    def test_output_integrity(self):
        """Test the integrity of the output format."""
        csv_to_line_protocol(self.sample_csv_path, self.output_path)
        with open(self.output_path, 'r') as f:
            content = f.read()
        self.assertTrue(content.startswith("temperature,"))
        self.assertTrue("1625097600" in content)