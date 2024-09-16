import os
import json


def concatenate_json_arrays(directory: str):
    combined_data = []

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a JSON file
        if filename.endswith('.json'):
            # Construct the full file path
            file_path = os.path.join(directory, filename)
            # Open and read the JSON file
            with open(file_path, 'r') as file:
                data = json.load(file)
                # Check if the question is a list (array at root)
                if isinstance(data, list):
                    combined_data.extend(data)
                else:
                    print(f"Warning: {filename} does not contain a root-level array.")

    return combined_data

