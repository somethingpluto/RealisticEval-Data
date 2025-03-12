import os
import yaml

def read_yaml(file_path: str):
    """
    Reads a YAML file and returns its content as a Python dictionary or list.

    Args:
        file_path (str): The path to the YAML file.

    Returns:
        dict or list: Parsed YAML content as a Python data structure.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        yaml.YAMLError: If there is an error parsing the YAML file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found")
    
    with open(file_path, 'r') as file:
        try:
            yaml_content = yaml.safe_load(file)
            return yaml_content
        except yaml.YAMLError as e:
            raise yaml.YAMLError(f"Error parsing YAML file: {e}") from e
import os
import unittest

import yaml


class TestReadYaml(unittest.TestCase):

    def setUp(self):
        """Create a temporary YAML file for testing."""
        self.valid_yaml_file = 'test_valid.yaml'
        self.invalid_yaml_file = 'test_invalid.yaml'
        self.non_existent_file = 'non_existent.yaml'

        # Valid YAML content
        with open(self.valid_yaml_file, 'w') as file:
            file.write("name: Example\nversion: 1.0\ndependencies:\n  - package1\n  - package2\n")

        # Invalid YAML content
        with open(self.invalid_yaml_file, 'w') as file:
            file.write("name: Example\nversion: 1.0\ndependencies:\n  - package1\n  - package2\ninvalid_yaml: \n - ")

    def tearDown(self):
        """Remove the temporary YAML files after testing."""
        if os.path.isfile(self.valid_yaml_file):
            os.remove(self.valid_yaml_file)
        if os.path.isfile(self.invalid_yaml_file):
            os.remove(self.invalid_yaml_file)

    def test_read_valid_yaml(self):
        """Test reading a valid YAML file."""
        expected_data = {
            'name': 'Example',
            'version': 1.0,
            'dependencies': ['package1', 'package2']
        }
        result = read_yaml(self.valid_yaml_file)
        self.assertEqual(result, expected_data)

    def test_file_not_found(self):
        """Test for FileNotFoundError when the file does not exist."""
        with self.assertRaises(FileNotFoundError):
            read_yaml(self.non_existent_file)


    def test_empty_yaml_file(self):
        """Test reading an empty YAML file."""
        empty_yaml_file = 'test_empty.yaml'
        with open(empty_yaml_file, 'w') as file:
            file.write("")  # Create an empty YAML file

        result = read_yaml(empty_yaml_file)
        self.assertIsNone(result)  # Expecting None for empty file

        os.remove(empty_yaml_file)  # Cleanup after the test
if __name__ == '__main__':
    unittest.main()