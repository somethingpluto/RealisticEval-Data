import csv
from typing import List


def read_csv(file_path: str) -> List[List[str]]:
    """
    Reads a CSV file and parses each line into a list of strings.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        List[List[str]]: A list of string lists, where each list represents a line from the CSV.
    """
    result = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            result.append(row)
    return result
import os
import unittest


class TestAnswer(unittest.TestCase):
    def setUp(self):
        # Create a temporary CSV file for testing
        self.test_file_path = 'test.csv'
        sample_csv_content = "Name,Age,Location\n" + \
                             "Alice,30,New York\n" + \
                             "Bob,25,Los Angeles\n" + \
                             "Charlie,35,Chicago\n"
        with open(self.test_file_path, 'w') as file:
            file.write(sample_csv_content)

    def test_read_valid_csv(self):
        result = read_csv(self.test_file_path)
        self.assertEqual(len(result), 4)  # 4 lines including the header
        self.assertEqual(result[0], ["Name", "Age", "Location"])  # Check header
        self.assertEqual(result[1], ["Alice", "30", "New York"])
        self.assertEqual(result[2], ["Bob", "25", "Los Angeles"])
        self.assertEqual(result[3], ["Charlie", "35", "Chicago"])

    def test_read_empty_csv(self):
        # Create an empty CSV file
        with open(self.test_file_path, 'w') as file:
            file.write("")
        result = read_csv(self.test_file_path)
        self.assertTrue(len(result) == 0)  # Expecting an empty list

    def test_read_csv_with_quotes(self):
        # Write CSV content with quoted fields
        content_with_quotes = '"Name","Age","Location"\n' + \
                              '"Alice","30","New York"\n' + \
                              '"Bob","25","Los Angeles"\n'
        with open(self.test_file_path, 'w') as file:
            file.write(content_with_quotes)
        result = read_csv(self.test_file_path)
        self.assertEqual(len(result), 3)  # 3 lines including the header
        self.assertEqual(result[0], ['Name', 'Age', 'Location'])

    def test_read_invalid_csv_file(self):
        with self.assertRaises(FileNotFoundError):
            read_csv('non_existent_file.csv')

    def test_read_csv_with_different_delimiters(self):
        # Write CSV content with semicolons instead of commas
        content_with_semicolons = "Name;Age;Location\n" + \
                                  "Alice;30;New York\n" + \
                                  "Bob;25;Los Angeles\n"
        with open(self.test_file_path, 'w') as file:
            file.write(content_with_semicolons)
        result = read_csv(self.test_file_path)
        self.assertEqual(len(result), 3)  # Expecting 3 lines
        self.assertEqual(result[0], ["Name;Age;Location"])

    def tearDown(self):
        # Clean up: remove test file after tests
        try:
            os.remove(self.test_file_path)
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    unittest.main()