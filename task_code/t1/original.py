import os
import json


def combine_json_files(directory_path:str, output_file:str) -> None:
    combined_data = []

    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'r', encoding="utf8") as file:
                data = json.load(file)
                if isinstance(data, list):
                    combined_data.extend(data)
                    print(f"Adding {filename} into database...")
                else:
                    print(f"Warning: File '{filename}' does not contain a list at the root level and will be skipped.")

    with open(output_file, 'w') as outfile:
        json.dump(combined_data, outfile, indent=4)
