import yaml
import json


def convert_yaml_to_json(yaml_file: str, json_file: str) -> None:
    """
    Convert a YAML file to a JSON file.

    :param yaml_file: Path to the input YAML file.
    :param json_file: Path to the output JSON file.
    """
    # Read the YAML file
    with open(yaml_file, 'r', encoding='utf-8') as yf:
        yaml_data = yaml.safe_load(yf)

    # Write the question to a JSON file
    with open(json_file, 'w', encoding='utf-8') as jf:
        json.dump(yaml_data, jf, indent=4)