import os

def modify_line_in_file(file_path: str, line_number: int, new_value: str) -> None:
    """
    Modifies a specific line in the given file.

    Args:
        file_path (str): The path of the file to be modified.
        line_number (int): The line number to be modified (1-based index).
        new_value (str): The new value to update the line with.

    Returns:

    """
    try:
        with open(file_path, 'r+') as file:
            lines = file.readlines()
            if line_number <= 0 or line_number > len(lines):
                raise ValueError("Invalid line number")

            lines[line_number - 1] = new_value + lines[line_number - 1][lines[line_number - 1].index('\n')]
            file.seek(0)
            file.truncate()
            file.writelines(lines)
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_path}' not found.")
    except ValueError as e:
        raise ValueError(e)
import os
import unittest


class TestAnswer(unittest.TestCase):
    TEST_FILE = "testFile.txt"

    def setUp(self):
        # Create a test file with initial content
        with open(self.TEST_FILE, 'w') as writer:
            writer.write("Line 1\n")
            writer.write("Line 2\n")
            writer.write("Line 3\n")

    def tearDown(self):
        # Clean up the test file after each test
        try:
            os.remove(self.TEST_FILE)
        except FileNotFoundError:
            pass  # File might already be deleted

    def test_modify_line_success(self):
        modify_line_in_file(self.TEST_FILE, 2, "Updated Line 2")
        with open(self.TEST_FILE, 'r') as reader:
            self.assertEqual("Line 1\n", reader.readline())
            self.assertEqual("Updated Line 2\n", reader.readline())
            self.assertEqual("Line 3\n", reader.readline())

    def test_modify_first_line(self):
        modify_line_in_file(self.TEST_FILE, 1, "Updated Line 1")
        with open(self.TEST_FILE, 'r') as reader:
            self.assertEqual("Updated Line 1\n", reader.readline())
            self.assertEqual("Line 2\n", reader.readline())
            self.assertEqual("Line 3\n", reader.readline())

    def test_modify_last_line(self):
        modify_line_in_file(self.TEST_FILE, 3, "Updated Line 3")
        with open(self.TEST_FILE, 'r') as reader:
            self.assertEqual("Line 1\n", reader.readline())
            self.assertEqual("Line 2\n", reader.readline())
            self.assertEqual("Updated Line 3\n", reader.readline())

    def test_modify_non_existent_line(self):
        with self.assertRaises(Exception):
            modify_line_in_file(self.TEST_FILE, 4, "Should Fail")

    def test_modify_negative_line_number(self):
        with self.assertRaises(Exception):
            modify_line_in_file(self.TEST_FILE, 0, "Should Fail")

if __name__ == '__main__':
    unittest.main()