
def append_row_after_skip_row(file_handler, reader, row_candidate):
    """
    Appends a new row to a CSV file if there isn't a row with matching values in the first three columns.

    Args:
        file_handler: File handler of the CSV file opened in read-plus mode ('r+').
        reader: CSV reader object for reading existing rows.
        row_candidate: List containing the new row to be appended.

    Returns:

    """
    # Skip the first row
    reader.next()

    # Get the first three columns of the current row
    first_three_columns = reader.get_column_values(0, 1, 2)

    # Check if there's a row with matching values in the first three columns
    if not row_candidate:
        return

    # Append the new row to the end of the file
    new_row = row_candidate[0] + "," + "," + first_three_columns[0] + "," + first_three_columns[1]
    reader.append(new_row)

import csv
import io
import unittest


class TestAppendSkipRow(unittest.TestCase):

    def setUp(self):
        """Set up a mock CSV file using StringIO."""
        self.mock_file = io.StringIO()
        self.mock_file.write("Alice,30,USA\nBob,25,UK\nCharlie,35,Canada\n")
        self.mock_file.seek(0)  # Reset pointer to the start of the mock file
        self.reader = csv.reader(self.mock_file)

    def test_append_new_row(self):
        new_row = ['David', '28', 'Australia']
        append_row_after_skip_row(self.mock_file, self.reader, new_row)

        self.mock_file.seek(0)  # Reset pointer to read from the start
        result = list(csv.reader(self.mock_file))
        self.assertIn(new_row, result)

    def test_skip_different_values(self):
        new_row = ['Alice', '31', 'USA']  # Same name, different age
        append_row_after_skip_row(self.mock_file, self.reader, new_row)

        self.mock_file.seek(0)  # Reset pointer to read from the start
        result = list(csv.reader(self.mock_file))
        self.assertIn(new_row, result)

    def test_append_row_with_different_columns(self):
        new_row = ['Eve', '40', 'Australia', 'Engineer']
        append_row_after_skip_row(self.mock_file, self.reader, new_row)

        self.mock_file.seek(0)  # Reset pointer to read from the start
        result = list(csv.reader(self.mock_file))
        self.assertIn(new_row, result)

    def test_multiple_appends(self):
        new_rows = [
            ['Frank', '29', 'Germany'],
            ['Grace', '22', 'France']
        ]

        for row in new_rows:
            append_row_after_skip_row(self.mock_file, self.reader, row)
            self.mock_file.seek(0)  # Reset pointer for the next read
            self.reader = csv.reader(self.mock_file)  # Recreate the reader after each append

        self.mock_file.seek(0)  # Reset pointer to read from the start
        result = list(csv.reader(self.mock_file))
        for row in new_rows:
            self.assertIn(row, result)
if __name__ == '__main__':
    unittest.main()