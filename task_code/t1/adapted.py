import os
import json


def merge_json_list_data(input_dir: str, output_json: str) -> None:
    """
    Reads all the JSON files from the specified directory and merges the data in those files into a list
    :param input_dir: json file dir path
    :param output_json:
    :return:
    """
    combined_data = []

    for file_name in os.listdir(input_dir):
        if file_name.endswith('.json'):
            file_path = os.path.join(input_dir, file_name)
            with open(file_path, 'r', encoding="utf8") as file:
                try:
                    data = json.load(file)
                    if isinstance(data, list):
                        combined_data.extend(data)
                        print(f"Added {file_name} to the combined data.")
                    else:
                        print(f"Skipped: {file_name} (root is not a list)")
                except json.JSONDecodeError:
                    print(f"Error: {file_name} is not a valid JSON file and will be skipped.")

    with open(output_json, 'w', encoding="utf8") as output_file:
        json.dump(combined_data, output_file, indent=4)
