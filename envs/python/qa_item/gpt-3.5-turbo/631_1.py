from typing import List
import csv

def write_csv_to_file(strings: List[str], file_path: str):
    """
    Formats a list of strings into a single-line CSV string and writes it to a specified file.

    Args:
        strings (List[str]): List of strings to be formatted into CSV.
        file_path (str): The file path where the CSV string should be written.

    Returns:

    """
    csv_string = ','.join(strings)
    
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([csv_string])
import os
import unittest


class TestAnswer(unittest.TestCase):
    def setUp(self):
        self.test_file_path = "test_output.csv"  # Path for test output file

    def tearDown(self):
        # Delete the test file after each test
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def read_file(self, file_path):
        """Helper method to read file content as a string."""
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except IOError as e:
            self.fail(f"Failed to read file: {e}")

    def test_write_csv_to_file_with_multiple_strings(self):
        data = ["Apple", "Banana", "Cherry"]
        write_csv_to_file(data, self.test_file_path)
        # Assert the content of the file
        content = self.read_file(self.test_file_path)
        self.assertEqual("Apple,Banana,Cherry", content)

    def test_write_csv_to_file_with_single_string(self):
        data = ["Apple"]
        write_csv_to_file(data, self.test_file_path)
        # Assert the content of the file
        content = self.read_file(self.test_file_path)
        self.assertEqual("Apple", content)

    def test_write_csv_to_file_with_empty_list(self):
        data = []
        write_csv_to_file(data, self.test_file_path)
        # Assert the content of the file is empty
        content = self.read_file(self.test_file_path)
        self.assertEqual("", content)

    def test_write_csv_to_file_with_special_characters(self):
        data = ["Apple", "Banana, Cherry", "Date"]
        write_csv_to_file(data, self.test_file_path)
        # Assert the content of the file
        content = self.read_file(self.test_file_path)
        self.assertEqual("Apple,Banana, Cherry,Date", content)

    def test_write_csv_to_file_with_spaces(self):
        data = ["Apple ", " Banana", " Cherry "]
        write_csv_to_file(data, self.test_file_path)
        # Assert the content of the file with spaces
        content = self.read_file(self.test_file_path)
        self.assertEqual("Apple , Banana, Cherry ", content)

    def test_write_csv_to_file_with_file_overwrite(self):
        # First write to the file
        first_data = ["Apple", "Banana"]
        write_csv_to_file(first_data, self.test_file_path)

        # Now overwrite with new data
        second_data = ["Cherry", "Date"]
        write_csv_to_file(second_data, self.test_file_path)

        # Assert that the file now contains the new data
        content = self.read_file(self.test_file_path)
        self.assertEqual("Cherry,Date", content)
if __name__ == '__main__':
    unittest.main()