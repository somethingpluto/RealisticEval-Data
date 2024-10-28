import os
import json


def concatenate_json_arrays(directory: str):
    combined_data = []

    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                data = json.load(file)
                if isinstance(data, list):
                    combined_data.extend(data)
                else:
                    print(f"Warning: {filename} does not contain a root-level array.")

    return combined_data

