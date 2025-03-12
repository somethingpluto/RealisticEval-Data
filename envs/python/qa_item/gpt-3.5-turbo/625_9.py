from typing import List, Union

def read_data_from_file(path: str) -> List[Union[int, float, str]]:
    """
    Reads data from a specified file and determines the type of each line.
    This function processes each line of the specified file and attempts to convert it
    into either an integer, a floating-point number, or a string.

    Args:
        path (str): The path to the file to be read. The file should exist and be accessible for reading.

    Returns:
        list: A list containing the converted values of each line in the file. Each element
              can be an int, float, or str, depending on the content of the line.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If the program lacks permissions to read the file.
        IOError: If an I/O error occurs while reading the file.
    """
    result = []
    try:
        with open(path, 'r') as file:
            for line in file:
                line = line.strip()
                if line.isdigit():
                    result.append(int(line))
                elif '.' in line and all(char.isdigit() or char == '.' for char in line):
                    result.append(float(line))
                else:
                    result.append(line)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found at path: {path}") from e
    except PermissionError as e:
        raise PermissionError(f"Permission denied to read file at path: {path}") from e
    except IOError as e:
        raise IOError(f"I/O error occurred while reading the file at path: {path}") from e
    
    return result
import os
import unittest


class Tester(unittest.TestCase):

    def create_test_file(self, file_name, content):
        with open(file_name, 'w') as writer:
            writer.write(content)

    def test_read_valid_integers(self):
        file_path = "valid_integers.txt"
        self.create_test_file(file_path, "42\n-7\n0\n100\n")
        result = read_data_from_file(file_path)
        self.assertEqual(4, len(result))
        self.assertEqual(42, result[0])
        self.assertEqual(-7, result[1])
        self.assertEqual(0, result[2])
        self.assertEqual(100, result[3])
        os.remove(file_path)  # Clean up the test file

    def test_read_valid_floats(self):
        file_path = "valid_floats.txt"
        self.create_test_file(file_path, "3.14\n-0.001\n2.71828\n0.0\n")
        result = read_data_from_file(file_path)
        self.assertEqual(4, len(result))
        self.assertEqual(3.14, result[0])
        self.assertEqual(-0.001, result[1])
        self.assertEqual(2.71828, result[2])
        self.assertEqual(0.0, result[3])
        os.remove(file_path)  # Clean up the test file

    def test_read_mixed_data(self):
        file_path = "mixed_data.txt"
        self.create_test_file(file_path, "Hello\n42\n3.14\nWorld\n-19.99\n")
        result = read_data_from_file(file_path)
        self.assertEqual(5, len(result))
        self.assertEqual("Hello", result[0])
        self.assertEqual(42, result[1])
        self.assertEqual(3.14, result[2])
        self.assertEqual("World", result[3])
        self.assertEqual(-19.99, result[4])
        os.remove(file_path)  # Clean up the test file

    def test_read_empty_file(self):
        file_path = "empty_file.txt"
        self.create_test_file(file_path, "")
        result = read_data_from_file(file_path)
        self.assertEqual(0, len(result))
        os.remove(file_path)  # Clean up the test file

    def test_read_invalid_data(self):
        file_path = "invalid_data.txt"
        self.create_test_file(file_path, "Hello\n42a\n3.14.15\nWorld!\n")
        result = read_data_from_file(file_path)
        self.assertEqual(4, len(result))
        self.assertEqual("Hello", result[0])
        self.assertEqual("42a", result[1])
        self.assertEqual("3.14.15", result[2])
        self.assertEqual("World!", result[3])
        os.remove(file_path)  # Clean up the test file

if __name__ == '__main__':
    unittest.main()