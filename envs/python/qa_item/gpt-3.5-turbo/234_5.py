import csv

def append_or_skip_row(file_handler, reader, row_candidate):
    """
    Appends a new row to a CSV file if there isn't a row with matching values in the first three columns.

    Args:
        file_handler: File handler of the CSV file opened in read-plus mode ('r+').
        reader: CSV reader object for reading existing rows.
        row_candidate: List containing the new row to be appended.

    Returns:

    """
    file_handler.seek(0)  # Move the file pointer to the beginning for reading
    existing_rows = [row for row in reader]  # Read existing rows

    matching_row = [row for row in existing_rows if row[:3] == row_candidate[:3] ]  # Check if there is a row with matching values in first three columns

    if not matching_row:
        writer = csv.writer(file_handler)
        writer.writerow(row_candidate)  # Append the new row if no matching row is found

import csv
import io
import unittest


class TestAppendOrSkipRow(unittest.TestCase):

    def setUp(self):
        """Set up a mock CSV file using StringIO."""
        self.mock_file = io.StringIO()
        self.mock_file.write("Alice,30,USA\nBob,25,UK\nCharlie,35,Canada\n")
        self.mock_file.seek(0)  # Reset pointer to the start of the mock file
        self.reader = csv.reader(self.mock_file)

    def test_append_new_row(self):
        """Test appending a new row when there are no matching values."""
        new_row = ['David', '28', 'Australia']
        append_or_skip_row(self.mock_file, self.reader, new_row)

        self.mock_file.seek(0)  # Reset pointer to read from the start
        result = list(csv.reader(self.mock_file))
        self.assertIn(new_row, result)

    def test_skip_different_values(self):
        """Test appending a new row with different values."""
        new_row = ['Alice', '31', 'USA']  # Same name, different age
        append_or_skip_row(self.mock_file, self.reader, new_row)

        self.mock_file.seek(0)  # Reset pointer to read from the start
        result = list(csv.reader(self.mock_file))
        self.assertIn(new_row, result)

    def test_append_row_with_different_columns(self):
        """Test appending a row with different values in the first three columns."""
        new_row = ['Eve', '40', 'Australia', 'Engineer']
        append_or_skip_row(self.mock_file, self.reader, new_row)

        self.mock_file.seek(0)  # Reset pointer to read from the start
        result = list(csv.reader(self.mock_file))
        self.assertIn(new_row, result)

    def test_multiple_appends(self):
        """Test appending multiple new rows correctly."""
        new_rows = [
            ['Frank', '29', 'Germany'],
            ['Grace', '22', 'France']
        ]

        for row in new_rows:
            append_or_skip_row(self.mock_file, self.reader, row)
            self.mock_file.seek(0)  # Reset pointer for the next read
            self.reader = csv.reader(self.mock_file)  # Recreate the reader after each append

        self.mock_file.seek(0)  # Reset pointer to read from the start
        result = list(csv.reader(self.mock_file))
        for row in new_rows:
            self.assertIn(row, result)
if __name__ == '__main__':
    unittest.main()