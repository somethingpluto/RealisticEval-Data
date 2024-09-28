import yaml
import os


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
    # Check if the file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    with open(file_path, "r") as file:
        try:
            # Load the YAML file content
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as e:
            raise yaml.YAMLError(f"Error parsing YAML file: {e}")
