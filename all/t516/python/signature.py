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