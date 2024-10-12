import json


def save_as_json(data, output_file_path):
    """
    Converts the data object to JSON format and saves it to the specified file path.

    Args:
        data (dict): The data object to be converted to JSON.
        output_file_path (str): The file path where the JSON will be saved.
    """
    try:
        # Convert data to JSON string with 2-space indentation
        json_data = json.dumps(data, indent=2)

        # Write the JSON string to the specified file path
        with open(output_file_path, 'w', encoding='utf-8') as json_file:
            json_file.write(json_data)

        print(f"Data successfully saved to {output_file_path}")
    except Exception as error:
        print(f"Error saving data to file: {error}")
