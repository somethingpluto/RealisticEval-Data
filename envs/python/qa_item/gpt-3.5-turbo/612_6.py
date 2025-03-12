import os

def find_and_replace_in_file(file_path:str, search_string:str, replace_string:str):
    try:
        with open(file_path, 'r') as file:
            file_data = file.read()
        
        file_data = file_data.replace(search_string, replace_string)
        
        with open(file_path, 'w') as file:
            file.write(file_data)
    
    except IOError as e:
        raise IOError("An I/O error occurred: {}".format(str(e)))
import os
import unittest


class TestFindAndReplace(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for the tests
        self.temp_dir = os.path.join(os.path.dirname(__file__), 'temp')
        os.makedirs(self.temp_dir, exist_ok=True)

    def tearDown(self):
        # Remove the temporary directory after tests
        for file in os.listdir(self.temp_dir):
            os.remove(os.path.join(self.temp_dir, file))
        os.rmdir(self.temp_dir)

    # Test case 1: Basic find and replace
    def test_find_and_replace_basic(self):
        file_path = os.path.join(self.temp_dir, "testfile.txt")
        with open(file_path, 'w') as file:
            file.writelines(["Hello World\n", "Goodbye World\n"])

        find_and_replace_in_file(file_path, "World", "Java")

        with open(file_path, 'r') as file:
            result = file.readlines()

        self.assertEqual(result, ["Hello Java\n", "Goodbye Java\n"])

    # Test case 2: No occurrences of the search string
    def test_find_and_replace_no_occurrences(self):
        file_path = os.path.join(self.temp_dir, "testfile.txt")
        with open(file_path, 'w') as file:
            file.writelines(["Hello World\n", "Goodbye World\n"])

        find_and_replace_in_file(file_path, "Python", "Java")

        with open(file_path, 'r') as file:
            result = file.readlines()

        self.assertEqual(result, ["Hello World\n", "Goodbye World\n"])

    # Test case 3: Multiple occurrences in a single line
    def test_find_and_replace_multiple_occurrences(self):
        file_path = os.path.join(self.temp_dir, "testfile.txt")
        with open(file_path, 'w') as file:
            file.writelines(["Hello World World\n", "Goodbye World\n"])

        find_and_replace_in_file(file_path, "World", "Java")

        with open(file_path, 'r') as file:
            result = file.readlines()

        self.assertEqual(result, ["Hello Java Java\n", "Goodbye Java\n"])

    # Test case 4: Replace with an empty string
    def test_find_and_replace_with_empty_string(self):
        file_path = os.path.join(self.temp_dir, "testfile.txt")
        with open(file_path, 'w') as file:
            file.writelines(["Hello World\n", "Goodbye World\n"])

        find_and_replace_in_file(file_path, "World", "")

        with open(file_path, 'r') as file:
            result = file.readlines()

        self.assertEqual(result, ["Hello \n", "Goodbye \n"])

    # Test case 5: Empty file
    def test_find_and_replace_empty_file(self):
        file_path = os.path.join(self.temp_dir, "testfile.txt")
        with open(file_path, 'w') as file:
            file.writelines(["\n"])

        find_and_replace_in_file(file_path, "World", "Java")

        with open(file_path, 'r') as file:
            result = file.readlines()

        self.assertEqual(result, ["\n"])

if __name__ == '__main__':
    unittest.main()