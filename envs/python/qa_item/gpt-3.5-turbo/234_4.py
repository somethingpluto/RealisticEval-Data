import csv

def append_or_skip_row(file_handler, reader, row_candidate):
    # Convert row_candidate to a tuple for comparison
    candidate_tuple = tuple(row_candidate[:3])
    
    # Check if there is a row with matching values in the first three columns
    for row in reader:
        if tuple(row[:3]) == candidate_tuple:
            return
    
    # If no matching row is found, append the new row to the CSV file
    writer = csv.writer(file_handler)
    writer.writerow(row_candidate)
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