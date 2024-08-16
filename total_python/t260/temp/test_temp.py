import unittest
import csv
import os


class TestCleanCSV(unittest.TestCase):

    def setUp(self):
        """Create a sample CSV file for testing."""
        self.input_file_path = 'test_input.csv'
        self.output_file_path = 'test_output.csv'
        self.sample_data = [
            ['Name', 'Age', 'City', 'State'],
            ['Alice', '25', '', ''],
            ['Bob', '30', 'New York', 'NY'],
            ['Charlie', '', '', ''],
            ['David', '45', 'Los Angeles', '', '']
        ]
        with open(self.input_file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(self.sample_data)

    def tearDown(self):
        """Clean up files created during the test."""
        os.remove(self.input_file_path)
        os.remove(self.output_file_path)

    def test_clean_csv(self):
        """Test the cleaning functionality of the CSV."""
        clean_csv(self.input_file_path, self.output_file_path)
        with open(self.output_file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            result = list(reader)

        expected = [
            ['Name', 'Age', 'City', 'State'],
            ['Bob', '30', 'New York', 'NY'],
        ]
        self.assertEqual(result, expected)

    def test_empty_file(self):
        """Test with an empty input file."""
        with open(self.input_file_path, 'w', newline='', encoding='utf-8') as file:
            file.write('')
        clean_csv(self.input_file_path, self.output_file_path)
        self.assertFalse(os.path.getsize(self.output_file_path))

    def test_all_rows_invalid(self):
        """Test when all rows should be filtered out."""
        with open(self.input_file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows([['John', '', ''], ['Jane', '', '']])
        clean_csv(self.input_file_path, self.output_file_path)
        with open(self.output_file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            result = list(reader)
        self.assertEqual(result, [])

    def test_no_rows_filtered(self):
        """Test with no rows ending with two consecutive empty columns."""
        data = [['Paul', '42', 'Denver', 'CO'], ['Sara', '35', 'Boston', 'MA']]
        with open(self.input_file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        clean_csv(self.input_file_path, self.output_file_path)
        with open(self.output_file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            result = list(reader)
        self.assertEqual(result, data)

    def test_mixed_rows(self):
        """Test a file containing a mix of valid and invalid rows."""
        data = [
            ['Eve', '', ''],
            ['Adam', '28', 'Seattle', 'WA'],
            ['Noah', '32', '', '']
        ]
        expected = [
            ['Adam', '28', 'Seattle', 'WA']
        ]
        with open(self.input_file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        clean_csv(self.input_file_path, self.output_file_path)
        with open(self.output_file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            result = list(reader)
        self.assertEqual(result, expected)

import csv


def clean_csv(input_file_path, output_file_path):
    """
    Processes a CSV file, deleting rows that end with two consecutive empty columns.

    :param input_file_path: Path to the input CSV file.
    :param output_file_path: Path to the output CSV file where cleaned data will be stored.
    """
    with open(input_file_path, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        rows = list(reader)

    # Filter rows that do not end with two consecutive empty columns
    cleaned_rows = [row for row in rows if len(row) < 2 or (row[-1] != '' or row[-2] != '')]

    with open(output_file_path, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(cleaned_rows)
